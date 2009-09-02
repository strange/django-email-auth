=================
Django Email Auth
=================

Allow users to login using their email address instead of a username.

A Few Cautions
==============

Django allows emails to be blank and does not ensure that they are unique. The
authentication backend supplied with this application does it's best to deal
with this, but you should take your responsibility and handle emails with care.

Installation
============

1. Add ``email_auth`` to ``INSTALLED_APPS`` in your project's settings module.

2. Add the ``email_auth`` authentication backend to your project's settings::

    AUTHENTICATION_BACKENDS = (
        'email_auth.backends.ModelBackend',
    )

3. Add a URL-pattern to your project's urls module (before any other
   configurations that include the login view)::

    (r'^accounts/', include('email_auth.urls')),


Configuration
=============

There are no settings in particular associated with this application.

Worth noting here is that the ``login`` view (intended to replace the default
Django login-view) takes an argument ``form_class`` that allows you to specify
a custom login form.

TODO
====

* It might be more elegant to just add a new argument (email) to the
  authenticate-method instead of using the old one for emails.
