from Models import global_variables

class Friends:
    user = None

    def __init__(self, user):
        self.user = user

        self.con = self.user.con
        self.cur = self.con.cursor()

    def addFriend(self, friendEmail):
        status = global_variables.DISCONN
        id_friend = self.cur.execute("SELECT id_friend FROM friends WHERE friend_email = ?",(friendEmail,))

        if id_friend.fetchone() is None:
            self.cur.execute("INSERT INTO friends (id_user,"
                                            + "friend_email,"
                                            + "status) values (?,"
                                                            + "?,"
                                                            + "?);",
                        (self.user.id_user,
                         friendEmail,
                         status)
            )
        self.con.commit()

    def lastTenMessages(self, friendEmail):
        friendID = self.getFriendID(friendEmail)
        return self.cur.execute("SELECT message_text, status FROM messages WHERE id_friend = ? ORDER BY id_message ASC LIMIT 10;", (friendID,)).fetchall()

    def getFriendID(self, friendEmail):
        result = self.cur.execute("SELECT id_friend FROM friends WHERE friend_email = ?", (friendEmail,)).fetchone()
        if result:
            return result[0]
        else:
            return result
    