import pika, os, sys
import pyrebase, requests, json
from dotenv import load_dotenv

load_dotenv()
CONFIG = json.loads(os.environ["CONFIG"])

class LoginServer:
    Config = CONFIG
    error = None
    thread = None

    def __init__(self):
        self.firebase = pyrebase.initialize_app(self.Config)
        self.auth = self.firebase.auth()

    def register(self, email, password):
        self.email = email
        self.password = password

        try:
            user = self.auth.create_user_with_email_and_password(self.email, self.password)
            self.error = None
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            self.error = json.loads(error_json)['error']['message']
        
    def login(self, email, password):
        self.email = email
        self.password = password

        try:
            user = self.auth.sign_in_with_email_and_password(self.email, self.password)
            self.error = None
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            self.error = json.loads(error_json)['error']['message']

    def addFriend(self, email):
        try:
            user = self.auth.sign_in_with_email_and_password(email, "0")
            self.error = None
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            self.error = json.loads(error_json)['error']['message']