from app import models
from app import bucket
import unittest


class CreateBuckTestCase(unittest.TestCase):
    def setUp(self):
        self.application = bucket.Application()

    def tearDown(self):
        pass

    def test_cannot_create_with_no_data_provided(self):
        self.assertFalse(self.application.create_buck_list())

    def test_cannot_create_with_invalid_data_provided(self):
        self.assertFalse(self.application.create_buck_list())
