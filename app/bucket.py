class BucketList(object):
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.items = {}


    def add_item(self, list_item):
        self.items[list_item.id] = list_item

    def remove_item(self, item_id):
        self.
