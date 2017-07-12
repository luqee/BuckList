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
        self.application.create_bucket_list('luke@gmail.com', self.bucklist)

    def tearDown(self):
        self.application = None
        self.user = None
        self.bucklist = None

    def test_cannot_create_item_with_no_data_provided(self):
        ''' Test to check that a user cannot create an item with empty parameters'''
        bucklist_item = models.BucketListItem(' ', ' ', ' ')
        self.assertEqual(self.application.create_bucket_list_item('luke@gmail.com', bucklist_item, 1), 'Invalid data')

    def test_cannot_create_with_invalid_data_provided(self):
        ''' Test to check that a user cannot create an item with invalid parameters'''
        bucklist_item = models.BucketListItem('item1', 'my first item on list', ' ')
        self.assertEqual(self.application.create_bucket_list_item('luke@gmail.com', bucklist_item, 1), 'Invalid data')

    def test_can_create_with_valid_data_provided(self):
        ''' Test to check that a user is able to create an item with valid parameters'''
        bucklist_item = models.BucketListItem('item1', 'my first item on list', '2/3/17')
        self.assertTrue(self.application.create_bucket_list_item('luke@gmail.com', bucklist_item, 1))
