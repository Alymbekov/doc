from imaster.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class SignUpForm(UserCreationForm):
    # full_name = forms.CharField(max_length=50, required=True, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


