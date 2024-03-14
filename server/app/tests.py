import unittest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

class TestUsersEndpoints(unittest.TestCase):
    
    def test_get_users(self):
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
