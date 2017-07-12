from app import models
from app import bucket
import unittest


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()
        self.user = models.User('luke', 'nzangu',
            'luke@gmail.com', 'pass')
        self.application.register_user(self.user)


    def tearDown(self):
        self.application = None
        self.user = None

    def test_user_cannot_login_with_empty_password(self):
        ''' Test to check that a user cannot login with an empty password'''
        self.assertFalse(self.application.login_user('luke@gmail.com', ''))

    def test_user_cannot_login_without_email(self):
        ''' Test to check that a user cannot login with an empty email address'''
        self.assertFalse(self.application.login_user('', 'pass'))
