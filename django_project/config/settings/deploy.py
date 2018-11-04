from .common import *


config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_DATA).read())

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = config_secret_deploy['DATABASES']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

WSGI_APPLICATION = 'config.wsgi.deploy.application'
