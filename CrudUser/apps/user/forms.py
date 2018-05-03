from django import forms
from apps.user.models import  User

class UserForm(forms.ModelForm):

    class Meta:
        model= User

        fields=[
            'name',
            'age',
            'birthday',
        ]

        labels={
            'name':'Nombre',
            'age':'Edad',
            'birthday':'Fecha de nacimiento',
        }

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'birthday':forms.TextInput(attrs={'class':'form-control'}),
        }
