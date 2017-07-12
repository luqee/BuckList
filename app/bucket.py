class Application(object):
    ''' This class models a bucket list application

    It provides functionalities for users to register and log in
    One can also create and delete bucketlist and items
    '''

    # Dictionary mapping an email address to a User object
    _email_to_user_map = {}
    # A list of signed in user's email address
    _signed_in_users = []


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Application, cls).__new__(cls)
        return cls.instance

    def register_user(self, user):
        '''
        This method takes the user object to register to the application
        and adds the object to _email_to_user_map dictionary.
        It returns the string "Email exists" if user is already registered
        or the the string "Registered" if successfully registered.
        '''
        if user.f_name == ' ':
            return 'First name empty'
        elif user.email == ' ':
            return 'Provide Email'
        elif user.password == ' ':
            return 'Provide password'
        elif user.email in self._email_to_user_map.keys():
            return 'Email exists'
        else:
            self._email_to_user_map[user.email] = user
            return 'Registered'

    def login_user(self, email, password):
        '''
        This method takes the email address and the password as credentials
        and checks from the  _email_to_user_map if the user exists.
        If so the user's email addreess
        is added to the list of logged in users and
        the function returns True. It returns False otherwise.
        '''
        if email in self._email_to_user_map.keys():
            if password == self._email_to_user_map[email].password and password not in self._signed_in_users:
                self._signed_in_users.append(email)
                return True
            else:
                return False
    
    def logout_user(self, email):
        '''
        This method takes the user's email address as an argument
        and cheks if they are registered and are signed in and if so
        the user is removed from the signed in users list.
        '''
        if email in self._email_to_user_map.keys():
            if email in self._signed_in_users:
                self._signed_in_users.remove(email)
                return True
        else:
            return False

    def create_bucket_list(self, email, bucklist):
        '''
        This method takes email and bucket list object
        as parameters and inserts both in the _email_to_bucket_list_map
        provided the email exists in the _email_to_user_map and.
        '''
        if bucklist.name == ' ' or bucklist.description == ' ' or bucklist.date == ' ':
            return 'Invalid data'
        if email in self._email_to_user_map.keys():
            user = self._email_to_user_map[email]
            bucklist.id = len(user.buck_lists) + 1
            user.buck_lists.append(bucklist)
            return True
        return False

    def edit_bucket_list(self, email, bucklist_id, new_bucket):
        '''
        This method takes email, bucketlist id 
        and a bucket list object as parameters and edits the
        given bucket id item.

        params: email
        params: Bucketlist Id
        params: Bucketlist object
        '''
        if new_bucket.name == ' ' or new_bucket.description == ' ' or new_bucket.date == ' ':
            return 'Invalid data'
        if email in self._email_to_user_map.keys():
            user = self._email_to_user_map[email]
            for buck in user.buck_lists:
                if buck.id == bucklist_id:
                    buck.name = new_bucket.name
                    buck.description = new_bucket.description
                    buck.date = new_bucket.date
                    return True
        return False

    def get_bucket_lists(self, email):
        ''' Get a user's bucket lists.

        This method takes email and returns the associated list
        of a user's bucketlist objects

        params: email
        '''
        if email in self._email_to_user_map.keys():
            user = self._email_to_user_map[email]
            bucklists = user.buck_lists
            return bucklists
        return 'Not registered'


    def remove_bucket_list(self, email, buck_id):
        ''' Remove a bucket list object.

        This method takes as arguments the variables email and bucket list id
        and returns True if the bucket list is deleted or
        False otherwise.

        param: email
        param: bucket list id
        '''
        if email in self._email_to_user_map.keys():
            for buck in self._email_to_user_map[email].buck_lists:
                if buck.id == buck_id:
                    self._email_to_user_map[email].buck_lists.remove(buck)
                    return True
        else:
            return False


    def view_bucket_list_items(self, email, buck_id):
        '''
        This method gets the bicketlist items

        params: email
        params: bucket list id
        '''
        if email in self._email_to_user_map.keys():
            for bucket_list in self._email_to_user_map[email].buck_lists:
                if bucket_list.id == buck_id:
                    return bucket_list.items
        else:
            return False


    def create_bucket_list_item(self, email, item, buck_id):
        ''' Creates a bucketlist item

        params: email of the logged in user
        params: item to add to bucket list
        params: bucket list id on which to add the item

        return: boolean
        '''
        if item.title == ' ' or item.desc == ' ' or item.date == ' ':
            return 'Invalid data'
        if email in self._email_to_user_map.keys():
            for buck in self._email_to_user_map[email].buck_lists:
                if buck.id == buck_id:
                    item.id = len(buck.items) +1
                    buck.items.append(item)
                    return True
        else:
            return False


    def remove_bucket_list_item(self, email, buck_id, item_id):
        ''' Removes an item from the bucket list

        params: email
        params: bucket list id
        params: item id

        return: boolean
        '''
        if email in self._email_to_user_map.keys():
            for buck in self._email_to_user_map[email].buck_lists:
                if buck.id == buck_id:
                    for item in buck.items:
                        if item.id == item_id:
                            buck.items.remove(item)
                            import pdb; pdb.set_trace()
                            return True
        else:
            return False
