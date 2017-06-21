from app import models
from app import bucket
import unittest

class ClassesTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()
        self.buck_list = models.BucketList('buclist1','first buck', '12/12/12')
        self.buck_list_item = models.BucketListItem('item1','item n one', '11/12/07')
        self.user = models.User('luke', 'nzangu', 'luke@gmail.com', 'pass')

    def tearDown(self):
        pass

    def test_register_user_is_successfull(self):
        self.assertTrue(self.application.register_user(self.user))

    def test_user_cannot_register_with_empty_first_name(self):
        user = models.User('', 'nzangu', 'luke@gmail.com', 'pass')
        self.assertFalse(self.application.register_user(user))

    def test_user_cannot_register_with_empty_email(self):
        user = models.User('luke', 'nzangu', '', 'pass')
        self.assertFalse(self.application.register_user(self.user))

    def test_user_cannot_register_without_password(self):
        user = models.User('luke', 'nzangu', 'luke@gmail.com', '')
        self.assertFalse(self.application.register_user(self.user))

    # def test_user_cannot_register_with_invalid_email(self):
    #     user = models.User('luke', 'nzangu', 'kfja:dof', 'pass')
    #     self.assertFalse(self.application.register_user(self.user))


    # def test_user_cannot_create_nameless_bucket_list(self):
    #     buck_list = models.BucketList('buclist1','first buck', '12/12/12')

    # def test_user_cannot_create_bucket_list(self):
    #     pass
