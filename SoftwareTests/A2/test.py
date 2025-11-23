import unittest
import docker
import time
from file import User, Db

class TestDb(unittest.TestCase):
    def setUp(self):
        self.client = docker.from_env()
        
        self.container = self.client.containers.run(
            "mongo:latest",
            ports={"27017/tcp": 27017},
            detach=True,
            remove=True  
        )
        
        time.sleep(5)
        
        self.db = Db("mongodb://localhost:27017/testdb")

    def tearDown(self):
        self.container.stop()
        self.client.close()

    def test_set_and_get_user(self):
        user = User("Alice", "alice@example.com")
        self.db.set_user(user)
        retrieved_user = self.db.get_user()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.name, user.name)
        self.assertEqual(retrieved_user.mail, user.mail)

if __name__ == "__main__":
    unittest.main()
