from django import forms
from .models import *

class MyForm1(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name','address','passwrd','username' ]

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'passwrd':forms.TextInput(attrs={'class':'form-control','type':'password'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),

            #'password':forms.CharField(widget=forms.PasswordInput)
        }

class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = SuppliersModel
        fields = ['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
           
        
        }