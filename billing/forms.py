from django.contrib.auth.models import User
from django.contrib.auth.fomrs import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']