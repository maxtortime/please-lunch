# Statement for enabling the development environment
DEBUG = True
WTF_CSRF_ENABLED = True
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:n61cde5173@localhost/please-lunch'

DATABASE_CONNECT_OPTIONS = {}

# UPLOAD_FOLDER
UPLOAD_FOLDER = 'app/static/uploads/'

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "super-secret"
SECURITY_REGISTERABLE =  True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'X2LGFS1AI39VRWYCYMXG3L5F4GS8EE35WUB0YSVPX7SUFWP70ETI1G2ZV2LLQGJ8'
SECURITY_BLUEPRINT_NAME = 'auth'
SECURITY_URL_PREFIX = '/auth'
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_POST_LOGIN_VIEW = '/start/'
SECURITY_POST_REGISTER_VIEW = '/start/'


# for flask-social
SOCIAL_FACEBOOK = {
    'consumer_key': '684002831732805',
    'consumer_secret': '51d173f01a0290682be0af5db48550a6'
}


