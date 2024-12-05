from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import box
from .models import Box, Comment


class BoxForms(forms.ModelForm):
    # image = forms.ImageField()
    # details = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = Box
        fields = [
            'image',
            'details'
        ]

        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'title': 'upload image'}),
            'details': forms.TextInput(attrs={'class': 'form-control', 'accept': 'text/plain'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your comment here'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

