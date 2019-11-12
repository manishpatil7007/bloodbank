from django import forms
from django.core import validators

class Empform(forms.Form):
    ename=forms.CharField(
        label="Enter your name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-Control',
                'placeholder':'Your Name'
            }
        )
    )
    sal=forms.IntegerField(
        label="Enter Your Salary:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-Control',
                'placeholder':'Your salary'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobile number:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-Control',
                'placeholder':'your mobile number'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your Email Id:",
        widget=forms.EmailField(
            attrs={
                'class':'form-Control',
                'placeholder':'Your Email id is:'
            }
        )
    )
    location=forms.CharField(
        label="Enter your location:",
        widget=forms.CharField(
            attrs={
                'class':'form-Control',
                'placeholder':'Your location is:'
            }
        )
    )