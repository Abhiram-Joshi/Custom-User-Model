from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email','password','phone')

        help_texts = {
            'email':'',
            'password':'',
            'phone':'',
        }