import unittest
import docker
import time
from File import User, Db

class TestFile(unittest.TestCase):
    def setUp(self):
    self.client = docker.from_env()
    self.container = self.client.containers.run(
        "mongo:latest",
        ports={"27017/tcp": 27017},
        detach=True
    )
    time.sleep(2)

    self.db = Db("mongodb://localhost:27017/testdb")
    

