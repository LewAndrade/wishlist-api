from os import environ

TESTING = True
DEBUG = True

MONGODB_SETTINGS = {
    'host': str(environ.get('MONGODB_SETTINGS'))
}
