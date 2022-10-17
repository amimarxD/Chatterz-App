import pika, os, sys
from dotenv import load_dotenv
from Controllers.LoginServerController import LoginServer
from Controllers.AmqpController import AmqpConnection
from Models import UsersModel, FriendsModel, MessagesModel 

load_dotenv()
HOSTNAME = os.environ["HOSTNAME"]

class Controller:
    loginServer = None

    userLocalDB = None
    friendLocalDB = None
    messageLocalDB = None

    email = None
    friendEmail = None
    

    def __init__(self):
        self.mq = AmqpConnection(hostname=HOSTNAME)
        self.mq.connect()
        self.loginServer = LoginServer()

    @staticmethod
    def register(email, password):

        # Message acknowledgment
        # Durable queue and durable message
        # Fair dispatch : do not dispatch a new message to a destination until it has processed and acknowledged the previous one
        # Topics
        loginServer = LoginServer()
        loginServer.register(email, password)
        if loginServer.error == None:
            # Stocking user info in the Local Database (SQLite)
            userLocalDB = UsersModel.Users()
            userLocalDB.register(email)
            

    def login(self, email, password):
        self.email = email

        self.loginServer.login(self.email, password)
        if self.loginServer.error == None:
            # Stocking user status (connected) in the Local Database
            self.userLocalDB = UsersModel.Users()
            self.userLocalDB.login(self.email)
            self.friendLocalDB = FriendsModel.Friends(self.userLocalDB)
            self.messageLocalDB = MessagesModel.Messages(self.friendLocalDB)

            # Establishing an open connection through the RabbitMQ node to recieve messagees
            binding_key = self.email+".*.*"
            result = self.mq.setup_queues(binding_key)

            def recieveMessage(ch, method, properties, body):
                print("[x] %r -> %r" % (method.routing_key, body))
                friendEmail = method.routing_key.replace(self.email+".", "")
                recievedMessage = body
                ch.basic_ack(delivery_tag = method.delivery_tag) 
                added_friend = self.messageLocalDB.recieveMessage(friendEmail, recievedMessage)
                if not added_friend:
                    self.addFriend(friendEmail)

            self.mq.consume(callback=recieveMessage, result=result)
        
    def addFriend(self, friendEmail):
        self.friendEmail = friendEmail
        self.loginServer.addFriend(self.friendEmail)
        if self.loginServer.error == 'INVALID_PASSWORD':
            self.friendLocalDB.addFriend(self.friendEmail)

    def showFriends(self):
        x = self.userLocalDB.showFriends()
        return x

    def showMessageHistory(self):
        return self.userLocalDB.showMessageHistory()

    def showLastTenMessages(self, friendEmail):
        return self.friendLocalDB.lastTenMessages(friendEmail)

    def sendMessage(self, friendEmail, message):
        routing_key = friendEmail + "." + self.email
        self.mq.send(message, routing_key)

        self.messageLocalDB.sendMessage(friendEmail, message)

    def disconnect(self):
        self.__del__()

    def __del__(self):
        self.mq.__del__()
        if self.userLocalDB.isConnected():
            self.userLocalDB.disconnect()