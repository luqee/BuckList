from app import app
from app import views
import unittest

class BucklistTestCase(unittest.TestCase):
    def setUp(self):
        #create test client
        self.tester = app.test_client()


    def test_correct_index_status_code(self):
        resp = self.tester.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_correct_register_status_code(self):
        resp = self.tester.get('/register')
        self.assertEqual(resp.status_code, 200)

    def test_correct_home_status_code(self):
        resp = self.tester.get('/home')
        self.assertEqual(resp.status_code, 200)

    def test_correct_login_status_code(self):
        resp = self.tester.get('/login')
        self.assertEqual(resp.status_code, 200)

    # def test_home_data(self):
    #     pass


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
