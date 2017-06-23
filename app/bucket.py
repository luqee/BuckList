class Application(object):
    # Dictionary mapping an email address to a User object
    _email_to_user_map = {}
    # Dictionary mapping an email address to a list of user's BucketLists object
    _email_to_bucket_list_map = {}





    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Application, cls).__new__(cls)
        return cls.instance

    def register_user(self, user):
        if user.email in self._email_to_user_map.keys():
            return False
        else:
            self._email_to_user_map[user.email] = user
            return True

    def login_user(self, email, password):
        if password == '':
            return False
        elif email == '':
            return False
        for ema in self._email_to_user_map.keys():
            if ema == email:
                if password == _email_to_user_map[email].password
                return True
            else:
                pass
        return False

    '''
    This method takes email and bucket list object
    as parameters and inserts both in the _email_to_bucket_list_map
    provided the email exists in the _email_to_user_map and .
    '''
    def create_bucket_list(self, email, bucklist):
        if email in self._email_to_user_map.keys():
            bucklist.id = len(_email_to_bucket_list_map[email]) + 1
            _email_to_bucket_list_map[email].append(bucklist)
            return True
        else:
            return False

    '''
    This method takes email and returns the associated list
    of bucketlist objects
    '''
    def get_bucket_list(self, email):
        if email in self._email_to_bucket_list_map.keys():
            bucklist = self._email_to_bucket_list_map[email]
            return bucklist
        else:
            return False

    def view_bucket_list_items(email, buck_id):
        if email in self._email_to_bucket_list_map.keys():
            for buck in _email_to_bucket_list_map[email]:
                if buck.id == buck_id:
                    return buck.items
                    break
        else:
            return False


    def create_bucket_list_item(email, item, buck_id):
        if email in self._email_to_bucket_list_map.keys():
            for buck in _email_to_bucket_list_map[email]:
                if buck.id == buck_id:
                    i = len(buck.items) +1
                    item.id = i
                    buck.items.append(item)
                    return True
        else:
            return False


    def remove_bucket_list_item(email, buck_id, item_id):
        if email in self._email_to_bucket_list_map.keys():
            for buck in _email_to_bucket_list_map[email]:
                if buck.id == buck_id:
                    i = _email_to_bucket_list_map.index(buck)
                    del _email_to_bucket_list_map[i]
                    return True
                    break
        else:
            return False


    def remove_bucket_list(email, buck_id):
        if email in self._email_to_bucket_list_map.keys():
            for buck in _email_to_bucket_list_map[email]:
                if buck.id == buck_id:
                    i = _email_to_bucket_list_map.index(buck)
                    del _email_to_bucket_list_map[i]
                    return True
                    break
        else:
            return False
