from django import forms

class Empform(forms.Form):
    ename=forms.CharField(
        label="Enter your name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name is :'
            }
        )
    )
    salary=forms.IntegerField(
        label='Enter your salary:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your salary is :'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter your mobile number:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile number:'
            }
        )
    )
    email=forms.EmailField(
        label='enter your email field:',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your email is:'
            }
        )
    )
    location=forms.CharField(
        label='enter your location:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your location is :'
            }
        )
    )
