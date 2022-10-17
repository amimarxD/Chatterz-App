import pika, os, sys
import threading
import functools
from retry import retry
from dotenv import load_dotenv

load_dotenv()
PORT = os.environ["PORT"]

def on_message(ch, method, properties, body):
    print("[x] %r -> %r" % (method.routing_key, body))

class AmqpConnection:
    def __init__(self, hostname='localhost', port=PORT):
        self.hostname = hostname
        self.port = port
        self.connection = None
        self.channel = None    
    
    def connect(self):
        if self.hostname == "localhost":
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        else:
            # Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
            self.url = os.environ.get('CLOUDAMQP_URL', self.hostname)
            self.params = pika.URLParameters(self.url)
            self.connection = pika.BlockingConnection(self.params)
        
        # Establishing an open connection through the RabbitMQ node to recieve messagees
        self.channel = self.connection.channel()

    def setup_queues(self, binding_key):
        self.channel.exchange_declare(
                exchange = "Chatterz",
                exchange_type = "topic"
        )
        result = self.channel.queue_declare(
                queue="",
                exclusive=False,
                durable=True
        )
        self.channel.queue_bind(
                queue=result.method.queue,
                exchange="Chatterz",
                routing_key=binding_key
        )
        return result
    
    def do_async(self, callback, *args, **kwargs):
        if self.connection.is_open:
            self.connection.add_callback_threadsafe(functools.partial(callback, *args, **kwargs))

    def send(self, payload, routing_key):
        if self.connection.is_open and self.channel.is_open:
            self.channel.basic_publish(
                exchange="Chatterz",
                routing_key=routing_key,
                body=payload,
                properties=pika.BasicProperties(
                         delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
                )
            )
    
    @retry(pika.exceptions.AMQPConnectionError, delay=1)
    def consume(self, callback=on_message, result=None):
        if self.connection.is_closed or self.channel.is_closed:
            self.connect()
            result = self.setup_queues()

        try:
            self.channel.basic_consume(queue=result.method.queue, 
                                       on_message_callback=lambda a,b,c,d: self.do_async(callback, ch=a, method=b, properties=c, body=d)
            )
            self.thread = threading.Thread(target=self.startConsuming)
            self.thread.start()

        except KeyboardInterrupt:
            print('Keyboard interrupt received')
            self.channel.stop_consuming()
            self.connection.close()
            os._exit(1)

        except pika.exceptions.ChannelClosedByBroker:
            print('Channel Closed By Broker Exception')
    
    def startConsuming(self):
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            print("Interrupted")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def __del__(self):
        self.channel.stop_consuming()
        self.thread.join()
        if self.channel.is_open:
            self.channel.close()
        if self.connection.is_open:
            self.connection.close()