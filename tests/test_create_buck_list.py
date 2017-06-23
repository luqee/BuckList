from app import models
from app import bucket
import unittest


class CreateBuckTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()

    def tearDown(self):
        pass

    def test_cannot_create_with_no_data_provided(self):
        bucklist = models.BucketList('', '', '')
        self.assertFalse(self.application.create_bucket_list('luke@gmail.com',bucklist))

    def test_cannot_create_with_invalid_data_provided(self):
        bucklist = models.BucketList('buck1', 'this is my first trip', 'date string')
        self.assertFalse(self.application.create_bucket_list('luke@gmail.com', bucklist))

    def test_can_create_with_valid_data_provided(self):
        bucklist = models.BucketList('buck1', 'this is my first trip', '2/3/17')
        self.assertFalse(self.application.create_bucket_list('luke@gmail.com', bucklist))
