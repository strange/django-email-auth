#!/usr/bin/env python
#encoding: utf-8

from distutils.core import setup

setup(
    name='django-email-auth',
    version='0.1',
    description='Allow users to login using their email address instead of a username.',
    author='Gustaf Sjöberg',
    author_email='gs@distrop.com',
    packages=['email_auth'],
)
