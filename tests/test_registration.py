from app import models
from app import bucket
import unittest


class ClassesTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()

    def tearDown(self):
        self.application = None

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
        user = models.User('luke', 'nzangu', 'lukaku@gmail.com', 'pass')
        user2 = models.User('user', 'imposter', 'lukaku@gmail.com', 'impoespass')
        self.assertEqual(self.application.register_user(user), 'Registered')
        self.assertEqual(self.application.register_user(user2), 'Email exists')

    def test_register_user_is_successfull_with_valid_data(self):
        user = models.User('luke', 'nzangu', 'lukey@gmail.com', 'pass')
        self.assertEqual(self.application.register_user(user), 'Registered')
