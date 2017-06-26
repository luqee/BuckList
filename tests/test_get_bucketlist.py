from app import models
from app import bucket
import unittest


class GetBuckTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()

    def tearDown(self):
        pass

    def test_cannot_get_bucket_list_of_non_existent_user(self):
        self.assertFalse(self.application.view_bucket_list_items('luke@gmail.com', 1))

    def test_gets_bucket_list_of_valid_user(self):
        self.assertFalse(self.application.view_bucket_list_items('luke@gmail.com',1))
