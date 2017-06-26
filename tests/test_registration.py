from app import models
from app import bucket
import unittest


class ClassesTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()
        self.user = models.User('luke', 'nzangu',
            'luke@gmail.com', 'pass')

    def tearDown(self):
        self.application = None
        self.user = None

    def test_user_cannot_register_with_empty_first_name(self):
        user = models.User(' ', 'nzangu', 'luke@gmail.com', 'pass')
        self.assertTrue(self.application.register_user(user), 'First name empty')

    def test_user_cannot_register_with_empty_email(self):
        user = models.User('luke', 'nzangu', ' ', 'pass')
        self.assertTrue(self.application.register_user(user), 'Provide Email')

    def test_user_cannot_register_without_password(self):
        user = models.User('luke', 'nzangu', 'luke@gmail.com', ' ')
        self.assertTrue(self.application.register_user(user), 'Provide password')
    
    def test_user_cannot_register_with_used_email(self):
        user = models.User('luke', 'nzangu', 'luke@gmail.com', 'pass')
        self.assertEqual(self.application.register_user(user), 'Email exists')

    def test_register_user_is_successfull_with_valid_data(self):
        user = models.User('luke', 'nzangu', 'luke@gmail.com', 'pass')
        self.assertEqual(self.application.register_user(user), 'Registered')