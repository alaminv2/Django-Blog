from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_login.models import UserProfile

class SignUpForms(UserCreationForm):
    email = forms.EmailField( label='Email Address', required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')


class ChangeProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'first_name', 'last_name', 'password'}


class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['pro_pic',]