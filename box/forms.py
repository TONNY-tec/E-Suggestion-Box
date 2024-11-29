from django import forms
from django.contrib.auth.forms import AuthenticationForm

import box
from box.models import Box


class BoxForms(forms.ModelForm):
    class Meta:
        model = Box
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'title': 'upload image'}),
            'details': forms.TextInput(attrs={'class': 'form-control', 'accept': 'text/plain'}),
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = Box
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

class RegisterForm(AuthenticationForm):
    class Meta:
        model = Box
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    def save(self):
        pass