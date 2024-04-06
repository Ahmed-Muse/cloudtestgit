from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm#this django form fields tha django creates automatically for us
from django.contrib.auth.models import User
from django.forms import fields#this is the model table for the users which django creates automatically for us
from .models import *


class AddUserDetailsForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = UserDetailsModel
        fields = ["username",'password']

class CreateUserForm(UserCreationForm):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
   
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',
                'password1','password2','is_superuser']#all these fields are from django
        #fields=['first_name','last_name',
                #'password1','password2']#all these fields are from django
        

class CreateCustomUserForm(UserCreationForm):
    
    class Meta:
        model=AllifmaalCustomUserModel
        fields=['email','admin','password1','password2','fname','lname']#all these fields are from django
        #fields=['first_name','last_name',
                #'password1','password2']#all these fields are from django
        widgets={
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Emial Address'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
            'password2':forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),
            'fname':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'lname':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),

            #'password1':forms.CharField(widget=forms.PasswordInput)
        }
##########################################################################################3


class CustomUserForm(forms.ModelForm):
    class Meta:
        model =AllifmaalCustomUserModel
        fields = ['email','password','category','admin' ]

        widgets={
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            #'admin':forms.BooleanField(attrs={'class':'form-control'}),
           
            'password':forms.TextInput(attrs={'class':'form-control','type':'password'}),
           

            #'password':forms.CharField(widget=forms.PasswordInput)
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model =UserProfileModel
        fields = ['name','title']

        widgets={
            'name':forms.Select(attrs={'class':'form-control','placeholder':'Email Address'}),
            
           
            'title':forms.TextInput(attrs={'class':'form-control'}),
           

            #'password':forms.CharField(widget=forms.PasswordInput)
        }



###################################


class UserEditForm(UserChangeForm):
   # username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    fname=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    lname=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    last_login=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    is_superuser=forms.CharField(max_length=50,widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    is_staff=forms.CharField(max_length=50,widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    is_active=forms.CharField(max_length=50,widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    date_joined=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   
    class Meta:
        model=AllifmaalCustomUserModel
        fields=['fname','lname','email','password','last_login','is_superuser','is_staff','is_active','date_joined']#all these fields are from django


