from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ecomapp.models import Carts,Placeorder


class SignUpForm(UserCreationForm):

    class  Meta:

        model=User

        fields=['first_name','last_name','username','password1','password2','email']


        widgets={
            "first_name":forms.TextInput(attrs={'class':'fnm','placeholder':'username'}),
            "last_name":forms.TextInput(attrs={'class':'lnm','placeholder':'password'}),
            "username":forms.TextInput(attrs={'class':'unm','placeholder':'password'}),
            "password1":forms.TextInput(attrs={'class':'psd1','placeholder':'password'}),
            "password2":forms.TextInput(attrs={'class':'psd2','placeholder':'password'}),
            "email":forms.TextInput(attrs={'class':'eml','placeholder':'password'}),
        }
    

class SignInForm(forms.Form):

    username=forms.CharField(max_length=100)
    password=forms.CharField( max_length=100)
    

    widgets={
        
        "username":forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
        "password":forms.TextInput(attrs={'class':'form-control1','placeholder':'password'}),
        
                }

class CartForm(forms.ModelForm):
    class Meta:

        model=Carts
        fields=['quantity']

class PlaceOrderForm(forms.ModelForm):

    class Meta:
        model=Placeorder
        fields=['address']
