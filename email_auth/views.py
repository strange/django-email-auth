from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache

from email_auth.forms import AuthenticationForm

def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          form_class=AuthenticationForm):
    """A replacement of ``django.contrib.auth.views.login`` that uses
    ``email_auth.forms.AuthenticationForm`` instead of the default
    authentication form.

    A custom form-class can be supplied via `form_class`.
    
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    form = form_class(data=request.POST or None)
    if form.is_valid():
        # Light security check -- make sure redirect_to isn't garbage.
        if not redirect_to or '//' in redirect_to or ' ' in redirect_to:
            redirect_to = settings.LOGIN_REDIRECT_URL

        from django.contrib.auth import login
        login(request, form.get_user())

        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(redirect_to)

    request.session.set_test_cookie()

    if Site._meta.installed:
        current_site = Site.objects.get_current()
    else:
        current_site = RequestSite(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }

    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))
login = never_cache(login)
