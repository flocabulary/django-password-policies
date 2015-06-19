from django import forms
from password_policies.forms.validators import validate_default


class PasswordPoliciesField(forms.CharField):
    """
A form field that validates a password using :ref:`api-validators`.
"""
    default_validators = [validate_default]

    def __init__(self, *args, **kwargs):
        if "widget" not in kwargs:
            kwargs["widget"] = forms.PasswordInput(render_value=False)
        super(PasswordPoliciesField, self).__init__(*args, **kwargs)
