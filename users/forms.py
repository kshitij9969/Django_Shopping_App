from django.forms import ModelForm
from users.models import UserProfile
from django.contrib.auth.admin import User
from django import forms


class UserProfileRegistrationForm(ModelForm):

    class Meta():
        model = UserProfile
        fields = ['user_contact', 'address']


class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta():
        model = User
        fields = ['username', 'email', 'password']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, required=False)











