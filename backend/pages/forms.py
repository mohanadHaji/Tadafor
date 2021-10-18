from django import forms

class CreateNewUser(forms.Form):
    name = forms.CharField(label="Name",max_length=20)
    password = forms.CharField(label="Password",max_length=20)