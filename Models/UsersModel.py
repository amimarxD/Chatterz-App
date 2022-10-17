import os
import sqlite3
from Models import global_variables

LOCAL_DB_NAME = os.environ["LOCAL_DB_NAME"]

class Users:
    id_user = None
    email = None
    status = global_variables.DISCONN
    ip_addr = None
    port = None

    def __init__(self):
        self.con = sqlite3.connect(LOCAL_DB_NAME, check_same_thread=False)
        self.cur = self.con.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS users(id_user INTEGER PRIMARY KEY AUTOINCREMENT," 
                                          + "email TEXT UNIQUE," 
                                          + "status TEXT," 
                                          + "ip_addr TEXT," 
                                          + "port INTEGER);"
                        )

        self.cur.execute("CREATE TABLE IF NOT EXISTS friends (id_friend INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT," 
                                             + "id_user INTEGER,"
                                             + "friend_email TEXT UNIQUE,"
                                             + "status TEXT,"
                                             + "CONSTRAINT fk_friend_user_id FOREIGN KEY (id_user) REFERENCES users(id_user));"              
        )

        self.cur.execute("CREATE TABLE IF NOT EXISTS messages(id_message INTEGER PRIMARY KEY AUTOINCREMENT," 
                                          + "id_user INTEGER,"
                                          + "id_friend INTEGER,"
                                          + "message_text TEXT,"
                                          + "status TEXT,"
                                          + "date_envoi DATE,"
                                          + "date_lecture DATE,"
                                          + "CONSTRAINT fk_message_user_id FOREIGN KEY (id_user) REFERENCES users(id_user));"
                        )
        self.con.commit()
        
    def login(self, email):
        self.email = email
        self.status = global_variables.CONN

        res = self.cur.execute("SELECT id_user FROM users WHERE email = ?;",(self.email,))
        if res.fetchone() is None:
            self.cur.execute("INSERT INTO users (email, status) values (?, ?);", 
                   (email, 
                    self.status)
            )
        else:
            self.cur.execute("UPDATE users SET status = ? WHERE id_user = ?;", 
                         (self.status, self.id_user)
        )
        self.id_user = self.cur.execute("SELECT id_user FROM users WHERE email = ?;",(self.email,)).fetchone()[0]
        self.con.commit()
        

    def disconnect(self):
        self.status = global_variables.DISCONN
        self.cur.execute("UPDATE users SET status = ? WHERE id_user =  ?;",
                         (self.status, self.id_user)
        )
        self.con.commit()
        self.cur.close()
        self.con.close()

    def isConnected(self):
        return self.status == global_variables.CONN

    @staticmethod
    def register(email):
        status = global_variables.DISCONN

        con = sqlite3.connect("chatterz.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users (email, status) values (?, ?);", 
                   (email, 
                    status)
        )
        con.commit()
        cur.close()
        con.close()

    def getUserID(self):
        return self.cur.execute("SELECT id_user FROM users WHERE email = ?", (self.email,)).fetchone()[0]
        
    def showFriends(self):
        result = self.cur.execute("SELECT friend_email FROM friends WHERE id_user = ?;", (self.id_user,)).fetchall()
        return [user[0] for user in result]

    def showMessageHistory(self):
        return self.cur.execute("SELECT friends.friend_email, messages.message_text FROM friends, messages WHERE messages.id_user = ? AND friends.id_friend = messages.id_friend AND messages.id_message IN (SELECT max(id_message) FROM messages GROUP BY id_friend);", (self.id_user,)).fetchall()