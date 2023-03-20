import os
import dj_database_url
from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['super-mart2.herokuapp.com']

# CSRF_TRUSTED_ORIGINS = ['https://levus-training.herokuapp.com', "http://localhost:3000",
#     "http://127.0.0.1:3000" ]

DATABASES = {
    'default': dj_database_url.config()
}

