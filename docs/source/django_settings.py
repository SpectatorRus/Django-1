"""
Minimal file so Sphinx can work with Django for autodocumenting.

Location: /docs/django_settings.py
"""

# SECRET_KEY for the documentation
SECRET_KEY = 'docs-super-secret'

# INSTALLED_APPS with these apps is necessary for Sphinx to build without warnings & errors
# Depending on your package, the list of apps may be different
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'expression',
    'str2words',
    'clicker'
]