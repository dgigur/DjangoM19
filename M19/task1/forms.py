from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    password = forms.CharField(min_length=8, label='password')
    repeat_password = forms.CharField(min_length=8, label='repeat_password')
    age = forms.CharField(max_length=8, label='age')
