from django.conf.urls.defaults import *

p = (
    (r'^login/$', 'email_auth.views.login', {}, 'auth_login'),
)

urlpatterns = patterns('', *p)
