from app import models
from app import bucket
import unittest


class CreateBuckTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()

    def tearDown(self):
        pass

    def test_cannot_get_bucket_list_of_non_existent_user(self):
        self.assertFalse(self.application.get_bucket_list('luke@gmail.com'))

    def test_gets_bucket_list_of_valid_user(self):
        self.assertFalse(self.application.get_bucket_list('luke@gmail.com'))
