from django.contrib.auth import get_user_model
User = get_user_model()

from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from phonenumber_field.modelfields import PhoneNumberField

from .models import Profile


class UserRegisterForm(UserCreationForm):
    number = PhoneNumberField()

    class Meta:
        model = User 
        fields = ['username','number','password1','password2']


class UserUpdateForm(forms.ModelForm):
    
    number = PhoneNumberField()

    class Meta:
        model = User 
        fields = ['username','number']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']