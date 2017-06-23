class Application(object):
    # Dictionary mapping an email address to a User object
    _email_to_user_map = {}
    # Dictionary mapping an email address to a user's BucketList object
    _email_to_bucket_list_map = {}





    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Application, cls).__new__(cls)
        return cls.instance

    def register_user(self, user):
        if user.email in self._email_to_user_map.keys():
            return False
        else:
            self._email_to_user_map[user.email] = (user)
            return True

    def login_user(self, email, password):
        if password == '':
            return False
        elif email == '':
            return False
        for k, v in self._email_to_user_map.items():
            if k == email:
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
        if email in self._email_to_user_map:
            _email_to_bucket_list_map[email] = bucklist
        else:
            return False

    '''
    This method
    '''
    def get_bucket_list(self, email):
        pass
        
    def edit_bucket_list(name):
        pass
