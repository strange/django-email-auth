"""

# Login fail. User does not exist.

>>> data = { 'email': 'name@example.com', 'password': 'password' }
>>> f = AuthenticationForm(data=data)
>>> f.is_valid()
False

# Login success. Email is unique.

>>> user = User.objects.create_user('glenn', 'name@example.com', 'password')
>>> data = { 'email': 'name@example.com', 'password': 'password' }
>>> f = AuthenticationForm(data=data)
>>> f.is_valid()
True

# Login success. Email is not unique but different passwords.

>>> user = User.objects.create_user('jerry', 'name@example.com', 'password2')
>>> data = { 'email': 'name@example.com', 'password': 'password2' }
>>> f = AuthenticationForm(data=data)
>>> f.is_valid()
True

# Login fail. Email is not unique and same passwords.

>>> try:
...     user = User.objects.create_user('jimmy', 'name@example.com',
...                                     'password2')
...     data = { 'email': 'name@example.com', 'password': 'password2' }
...     f = AuthenticationForm(data=data)
...     f.is_valid()
... except CouldNotAuthenticateError:
...     True
True

"""

from django.conf import settings
from django.contrib.auth.models import User

from email_auth.forms import AuthenticationForm
from email_auth.backends import CouldNotAuthenticateError

if __name__ == '__main__':
    import doctest
    doctest.testmod()
