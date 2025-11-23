from pymongo import MongoClient

class User:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

class Db:
    def __init__(self, conn_str, db_name="testdb"):
        self.client = MongoClient(conn_str)
        self.collection = self.client[db_name].users

    def set_user(self, user: User):
        self.collection.insert_one({"name": user.name, "mail": user.mail})

    def get_user(self):
        output = self.collection.find_one()
        if output:
            return User(output["name"], output["mail"])
        return None
