class Application(object):
    _email_to_user_map = {}
    _email_to_bucket_list_map = {}




    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Application, cls).__new__(cls)
        return cls.instance

    def register_user(self, user):
        if user.email in self._email_to_user_map.keys():
            return False
        else:
            self._email_to_user_map[user.email] = (user, 0)
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

    def create_bucket_list(email, bucklist):
        pass

    def edit_bucket_list(name):
        pass
