from django.core.exceptions import ValidationError
from django.forms import Form
from django.forms.fields import CharField, EmailField
from django.views.generic import FormView


class ChangePasswordForm(Form):
    password = CharField()
    confirm_password = CharField()
    email = EmailField()

    def clean(self):
        data = self.cleaned_data
        if data.get("password") != data.get("confirm_password"):
            raise ValidationError("No match password")
        data.pop("confirm_password")
        return data
