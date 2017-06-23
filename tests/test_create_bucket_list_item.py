from app import models
from app import bucket
import unittest


class CreateBuckTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()

    def tearDown(self):
        pass

    def test_cannot_create_item_with_no_data_provided(self):
        bucklist_item = models.BucketListItem('', '', '')
        self.assertFalse(self.application.create_bucket_list('luke@gmail.com',bucklist))

    def test_cannot_create_with_invalid_data_provided(self):
        bucklist_item = models.BucketListItem('item1', 'my first item on list', 'dkgndsgns')
        self.assertFalse(self.application.create_bucket_list('luke@gmail.com', bucklist))

    def test_can_create_with_valid_data_provided(self):
        bucklist_item = models.BucketListItem('item1', 'my first item on list', '2/3/17')
        self.assertFalse(self.application.create_bucket_list('luke@gmail.com', bucklist))
