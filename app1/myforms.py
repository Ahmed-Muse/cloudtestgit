from django import forms
from .models import *
class MyForm1(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name','address' ]

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','value':'item.name'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            
        }