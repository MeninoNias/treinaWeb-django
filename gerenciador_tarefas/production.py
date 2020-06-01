import django_heroku

DEBUG = False
ALLOWED_HOSTS = ['*']

django_heroku.settings(locals())