from app import app
from app import views
import unittest

class BucklistTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()



    def test_correct_status_code(self):
        resp = self.tester.get('/')
        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
