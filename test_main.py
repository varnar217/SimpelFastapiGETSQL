import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestApp(unittest.TestCase):

    def test_read_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_read_user(self):
        response = client.get("/plays/1")
        assert response.status_code == 200

    def test_read_all_users(self):
        response = client.get("/plays23")
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
