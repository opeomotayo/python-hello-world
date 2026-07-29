import unittest
from app import app, elapsed


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_root(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello World (Python)!", response.get_data(as_text=True))

    def test_root_content_type(self):
        response = self.client.get('/')

        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_elapsed_format(self):
        result = elapsed()

        # Expected format: H:MM:SS
        parts = result.split(":")

        self.assertEqual(len(parts), 3)
        self.assertTrue(parts[0].isdigit())
        self.assertTrue(parts[1].isdigit())
        self.assertTrue(parts[2].isdigit())


if __name__ == "__main__":
    unittest.main()
