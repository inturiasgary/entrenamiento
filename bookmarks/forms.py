#!/usr/bin/env python
from django import forms
class RegistrationForm(forms.Form):
  username = forms.CharField(label='Username', max_length=30)
  email = forms.EmailField(label='Email')
  password1 = forms.CharField(label='Contrase?a', widget=forms.PasswordInput())
  password2 = forms.CharField(label='Contrase?a (Nuevamente)',widget=forms.PasswordInput())