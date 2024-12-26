from django import forms


class Str2Words(forms.Form):
    words = forms.CharField(label="введите строку", max_length=100)
