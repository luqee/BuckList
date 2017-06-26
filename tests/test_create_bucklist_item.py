from app import models
from app import bucket
import unittest


class CreateBuckItemTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()
        self.user = models.User('luke', 'nzangu',
            'luke@gmail.com', 'pass')
        self.application.register_user(self.user)
        self.bucklist = models.BucketList('buck1',
            'this is my first trip', '2/3/17')

    def tearDown(self):
        pass

    def test_cannot_create_item_with_no_data_provided(self):
        bucklist_item = models.BucketListItem('', '', '')
        self.assertFalse(self.application.create_bucket_list_item('luke@gmail.com', bucklist_item, 1))

    def test_cannot_create_with_invalid_data_provided(self):
        bucklist_item = models.BucketListItem('item1', 'my first item on list', 'dkgndsgns')
        self.assertFalse(self.application.create_bucket_list_item('luke@gmail.com', bucklist_item, 1))

    def test_can_create_with_valid_data_provided(self):
        bucklist_item = models.BucketListItem('item1', 'my first item on list', '2/3/17')
        self.assertFalse(self.application.create_bucket_list_item('luke@gmail.com', bucklist_item, 1))
