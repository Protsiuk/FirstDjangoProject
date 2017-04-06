from django import forms
from account

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=10, max_length=20, widget=forms.TextInput(atr={"class": "password"}))



