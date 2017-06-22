class Application(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Application, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._email_to_user_map = {}

    def register_user(self, user):
        if user.email in self._email_to_user_map.keys():
            return False
        else:
            self._email_to_user_map[user.email] = (user, 0)
            return True

    def login_user(self, email, password):
        for k, v in self._email_to_user_map.items():
            if k == email:
                return True
            else:
                pass
        return False
