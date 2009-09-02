from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend as _ModelBackend

class CouldNotAuthenticateError(Exception):
    """Multiple accounts with the same email and the same password exit."""
    pass


class ModelBackend(_ModelBackend):
    def authenticate(self, username=None, password=None):
        """Allow ``Users`` to authenticate by email in addition to username.

        Be very careful if you allow at-signs in usernames as this backend
        will treat anything containing an at-sign as an email address.

        Proper measures should also be taken to ensure the uniqueness of
        email addresses as this is not done by Django.

        """
        if '@' in username:
            lookup = { 'email__iexact': username }
        else:
            lookup = { 'username': username }

        # There's no unique constraint on email addresses in the default
        # implementation of auth.User. Failing on MultipleObjectsReturned
        # is not really an option so we're testing the password against
        # all matches. Will raise CouldNotAuthenticateError if multiple
        # email addresses share the same password.
        matching_users = []
        for user in User.objects.filter(**lookup):
            if user.check_password(password):
                matching_users.append(user)
        
        if len(matching_users) == 1:
            return matching_users[0]
        elif len(matching_users) > 1:
            raise CouldNotAuthenticateError

        return None
