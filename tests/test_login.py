from app import models
from app import bucket
import unittest

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()

    def tearDown(self):
        pass

    def test_user_cannot_login_with_empty_password(self):
        self.assertFalse(self.application.login_user('luke@gmail.com', ''))

    def test_user_cannot_login_without_email(self):
        self.assertFalse(self.application.login_user('', 'pass'))
