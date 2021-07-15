from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length = 30, required = False)
    first_name = forms.CharField(max_length=30, required = False)
    last_name = forms.CharField(max_length=30, required = False)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
