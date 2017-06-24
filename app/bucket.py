class Application(object):
    # Dictionary mapping an email address to a User object
    _email_to_user_map = {}
    # A list of signed in user's email address
    _signed_in_users = []


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
        if email in self._email_to_user_map.keys():
            if password == self._email_to_user_map[email].password:
                self._signed_in_users.append(email)
                return True
            else:
                return False

    '''
    This method takes email and bucket list object
    as parameters and inserts both in the _email_to_bucket_list_map
    provided the email exists in the _email_to_user_map and.
    '''
    def create_bucket_list(self, email, bucklist):
        if email in self._email_to_user_map.keys():
            user = self._email_to_user_map[email]
            user.buck_lists.append(bucklist)
            return True
        else:
            return False

    '''
    This method takes email and returns the associated list
    of a user's bucketlist objects
    '''
    def get_bucket_lists(self, email):
        if email in self._email_to_user_map.keys():
            user = self._email_to_user_map[email]
            bucklists = user.buck_lists
            return bucklists
        else:
            return 0


    def remove_bucket_list(email, buck_id):
            if email in self._email_to_user_map.keys():
                for buck in self._email_to_user_map[email].buck_lists:
                    if buck.id == buck_id:
                        self._email_to_user_map[email].buck_lists.remove(buck)
                        return True
            else:
                return False


    def view_bucket_list_items(self, email, buck_id):
        if email in self._email_to_user_map.keys():
            for bucket_list in self._email_to_user_map[email].buck_lists
                if bucket_list.id == buck_id:
                    return bucket_list.items
        else:
            return False


    def create_bucket_list_item(self, email, item, buck_id):
        if email in self._email_to_user_map.keys():
            for buck in self._email_to_user_map[email].buck_lists:
                if buck.id == buck_id:
                    item.id = len(buck.items) +1
                    buck.items.append(item)
                    return True
        else:
            return False


    def remove_bucket_list_item(email, buck_id, item_id):
        if email in self._email_to_user_map.keys():
            for buck in _email_to_user_map[email].buck_lists:
                if buck.id == buck_id:
                    for item in buck.items:
                        if item.id == item_id:
                            buck.items.remove(item)
                            return True
        else:
            return False
