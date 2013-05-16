from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm as Form
from django.utils.translation import ugettext_lazy as _

class AuthenticationForm(Form):
    """Authenticate a ``User`` by email and password."""
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        del(self.fields['username'])
        self.fields.insert(0, 'email', forms.CharField(label=_(u"Email")))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(username=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(_("Please enter a correct email "
                                              "and password. Note that the "
                                              "password is case-sensitive."))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_("This account is inactive."))

        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError(_("Your Web browser doesn't "
                                              "appear to have cookies "
                                              "enabled. Cookies are required "
                                              "for logging in."))

        return self.cleaned_data
