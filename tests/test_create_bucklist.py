from app import models
from app import bucket
import unittest


class CreateBuckTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()
        self.user = models.User('luke', 'nzangu',
            'luke@gmail.com', 'pass')
        self.application.register_user(self.user)

    def tearDown(self):
        pass

    def test_cannot_create_with_no_data_provided(self):
        bucklist = models.BucketList(' ', ' ', ' ')
        self.assertTrue(self.application.create_bucket_list('luke@gmail.com',bucklist), 'Invalid data')

    def test_cannot_create_with_invalid_data_provided(self):
        bucklist = models.BucketList('buck1', 'this is my first trip', ' ')
        self.assertTrue(self.application.create_bucket_list('luke@gmail.com', bucklist), 'Invalid data')

    def test_can_create_with_valid_data_provided(self):
        bucklist = models.BucketList('buck1', 'this is my first trip', '2/3/17')
        self.assertTrue(self.application.create_bucket_list('luke@gmail.com', bucklist))
