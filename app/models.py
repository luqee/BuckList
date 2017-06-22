class User(object):
    # f_name = ''
    # l_name = ''
    # email = ''
    # password = ''
    # buck_lists = []

    def __init__(self,f_name, l_name, email, password):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password
        #A list of thee user's bucket lists
        self.buck_lists = []


    def store_buck_list(self, buck_list):
        pass

    def remove_buck_list(self, id):
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
