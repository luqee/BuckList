"""
This module is used to store the flask application
instance configuration.
"""
class Configuration(object): # Instruct Flask to run the application in DEBUG mode.
    """
    Class containing configuration for the flask application instance.
    """
    DEBUG = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'mysecret'
