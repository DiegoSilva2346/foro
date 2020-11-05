from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["blogsilva3.herokuapp.com"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbvcashr9e1mc7',     
        'USER':'paqwdwumfohzdq',    
        'PASSWORD':'80a0ec3eb9a3ae048f1e4f189a44f100bad0725137082e87516ed118f9869bfa',  
        'HOST':'ec2-35-168-77-215.compute-1.amazonaws.com',   
        'PORT': 5432,
    }
}
STATICFILES_DIR = (BASE_DIR,'static')