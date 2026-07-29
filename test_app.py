import unittest
from app import app


class TestApp(unittest.TestCase):

    def test_home_page(self):
        client = app.test_client()
        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello World (Python)!", response.text)


if __name__ == "__main__":
    unittest.main()

