from pymongo import MongoClient

class User:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

class Db:
    def __init__(self, conn_str):
        self.client = MongoClient(conn_str)
        self.collection = self.client.get_database().users

    def set_user(user: User):
        self.collection.insert_one({"name": user.name, "mail": user.mail})

    def get_user():
        output = self.collection.find_one()
        if output:
            return User(output["name"], output["mail"])
        return None
    