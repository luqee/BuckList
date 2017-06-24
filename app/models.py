class User(object):

    def __init__(self, f_name, l_name, email, password):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password
        # A list of thee user's bucket lists
        self.buck_lists = []


class BucketList(object):
    def __init__(self, name, descr, date):
        self.id = 0
        self.name = name
        self.description = descr
        self.date = date
        # list of bucket list items
        self.items = []


class BucketListItem(object):

    def __init__(self, title, descr, date):
        self.title = title
        self.desc = descr
        self.date = date
        self.id = 0
