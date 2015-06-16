from django import forms
from django.utils.module_loading import import_by_path

from password_policies.conf import settings

default_validators = map(import_by_path, settings.PASSWORD_DEFAULT_VALIDATORS)

class PasswordPoliciesField(forms.CharField):
    """
A form field that validates a password using :ref:`api-validators`.
"""
    default_validators = default_validators

    def __init__(self, *args, **kwargs):
        if "widget" not in kwargs:
            kwargs["widget"] = forms.PasswordInput(render_value=False)
        super(PasswordPoliciesField, self).__init__(*args, **kwargs)
