from django import forms


class Auth(forms.Form):
    username = forms.CharField(label="username",  max_length=50)
    password = forms.CharField(label="password",  max_length=50)

