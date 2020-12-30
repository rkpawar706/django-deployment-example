from django import forms
from .models import UserModel
from django.contrib.auth.models import User

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("email",'username',"password")

class Usermodelform(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ("portfolio_site","profile_image")