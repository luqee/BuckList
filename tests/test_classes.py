from app import models

import unittest

class ClassesTestCase(unittest.TestCase):
    def setUp(self):
        self.buck_list = models.BucketList()
        self.buck_list_item = models.BucketList()
        self.buck_list = models.BucketList()
