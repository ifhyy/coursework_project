from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import *


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'login-field'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'login-field'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'login-field'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'login-field'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'login-field'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'login-field'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email belongs to other user')
        return email


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'text', 'price', 'picture', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'login-field'}),
            'text': forms.Textarea(attrs={'class': 'login-field'}),
            'price': forms.NumberInput(attrs={'class': 'login-field'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Price should be positive')
        return price
