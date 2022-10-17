from datetime import datetime
from Models import global_variables

class Messages:
    user = None
    friend = None

    def __init__(self, friend):
        self.friend = friend
        self.user = self.friend.user

        self.con = self.friend.con
        self.cur = self.con.cursor()

    def sendMessage(self, friendEmail, message_text):
        status = global_variables.MSG_SENT
        date_envoi = str(datetime.now())
        date_lecture = None
        # datetime.datetime.strptime(str(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
        friendID = self.friend.getFriendID(friendEmail)

        self.cur.execute("INSERT INTO messages (id_user,"
                                            + " id_friend,"
                                            + " date_envoi,"
                                            + " date_lecture,"
                                            + " message_text,"
                                            + " status) VALUES (?,"
                                                             + "?," 
                                                             + "?,"
                                                             + "?,"
                                                             + "?,"
                                                             + "?);",
                        (self.user.id_user,
                         friendID,
                         date_envoi,
                         date_lecture,
                         message_text,
                         status)
        )
        self.con.commit()

    def recieveMessage(self, friendEmail, message_text, date_envoi=None):
        status = global_variables.MSG_RECVD
        message_text = message_text.decode("utf8")
        date_lecture = str(datetime.now())
        # datetime.datetime.strptime(str(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
        friendID = self.friend.getFriendID(friendEmail)

        if friendID:
            self.cur.execute("INSERT INTO messages (id_user,"
                                            + " id_friend,"
                                            + " date_envoi,"
                                            + " date_lecture,"
                                            + " message_text,"
                                            + " status) VALUES (?,"
                                                             + "?," 
                                                             + "?,"
                                                             + "?,"
                                                             + "?,"
                                                             + "?);",
                        (self.user.id_user,
                         friendID,
                         date_envoi,
                         date_lecture,
                         message_text,
                         status)
            )
            self.con.commit()
            return True
        else:
            return False