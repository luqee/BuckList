from app import app
from app import views
import unittest


class BucklistTestCase(unittest.TestCase):
    def setUp(self):
        # create test client
        self.tester = app.test_client()

    # def test_register(self):
    #     rv = self.register('luket', 'kanga', 'luke@gmail.com', 'password')
    #     assert b'You have been successfully registered' in rv.data
    
    # def test_login(self):
    #     rv = self.login('luke@gmail.com', 'password')
    #     assert b'You were successfully logged in' in rv.data

    def test_correct_index_status_code(self):
        resp = self.tester.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_correct_register_status_code(self):
        resp = self.tester.get('/register')
        self.assertEqual(resp.status_code, 200)

    def test_correct_home_status_code(self):
        resp = self.tester.get('/home', follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

    def test_correct_login_status_code(self):
        resp = self.tester.get('/login')
        self.assertEqual(resp.status_code, 200)
        
    def tearDown(self):
        pass
    
    # def register(self, fname, lname, email, password):
    #     return self.tester.post('/register', data=dict(
    #         first_name=fname,
    #         last_name=lname,
    #         email=email,
    #         password=password
    #     ), follow_redirects=True)

    # def login(self, email, password):
    #     return self.tester.post('/login', data=dict(
    #         email=email,
    #         password=password
    #     ), follow_redirects=True)

    # def logout(self):
    #     return self.tester.get('/logout', follow_redirects=True)