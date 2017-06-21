class User(object):

    def __init__(self,):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password


    def logout(self):
        pass

    def register(self):
        pass


class BucketList(object):

    def __init__(self, name, descr, date):
        self.name = name
        self.description = descr
        self.date = date
        #dictionary of tuples
        self.items = {}

    def add_item(self, item):
        pass

    def get_item(self, id):
        pass

    def remove_item(self, id):
        pass

    def update_item(self, item):
        pass


class BucketListItem(object):

    def __init__(self, title, descr, date):
        self.title = title
        self.desc = descr
        self.date = date
