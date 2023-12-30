from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, UserBankAccount
from .constant import GENDER_TYPE
from django.contrib.auth.forms import AuthenticationForm

class CustomUserLoginForm(AuthenticationForm):
  class Meta:
    model = CustomUser
    fields = ['email', 'password']
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    for field in self.fields:
        self.fields[field].widget.attrs.update({
            'class' : (
                'appearance-none block w-full bg-gray-200 '
                'text-gray-700 border border-gray-200 rounded '
                'py-3 px-4 leading-tight focus:outline-none '
                'focus:bg-white focus:border-gray-500'
            )
        })

class CustomUserCreationForm(UserCreationForm):
  username = forms.CharField(max_length=100)
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
  gender = forms.ChoiceField(choices=GENDER_TYPE)
  street_address = forms.CharField(max_length=100)
  city = forms.CharField(max_length= 100)
  postal_code = forms.IntegerField()
  country = forms.CharField(max_length=100)
  class Meta:
    model = CustomUser
    fields = ['email', 'username', 'first_name', 'last_name','password1', 'password2', 'birth_date', 'gender', 'street_address', 'city', 'postal_code', 'country']


  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    for field in self.fields:
        self.fields[field].widget.attrs.update({
            'class' : (
                'appearance-none block w-full bg-gray-200 '
                'text-gray-700 border border-gray-200 rounded '
                'py-3 px-4 leading-tight focus:outline-none '
                'focus:bg-white focus:border-gray-500'
            )
        })





class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = ['email', 'first_name', 'last_name']