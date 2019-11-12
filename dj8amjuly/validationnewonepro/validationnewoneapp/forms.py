from django import forms
from .models import RegistrationData


class RegistrationForm(forms.Form):
    firstname=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your firstname'
            }

        )

    )
    lastname=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your lasstname'
            }
        )
    )
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username is'
            }
        )
    )
    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'email'
            }
        )
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your password is'
            }
        )
    )
    password2=forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter confirm password.'
            }
        )

    )
    mobile=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter your mobile'
            }
        )

    )
    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=RegistrationData.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already take")
        elif len(username)<=5:
            raise forms.ValidationError("username must have more than 5 charcter")
        return username
    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=RegistrationData.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email name is already taken")
        elif not 'gmail.com' in email:
            raise forms.ValidationError("Email has to end with gmail.com")
        return email
    def clean_mobile(self):
        mobile=self.cleaned_data.get('mobile')
        mob=RegistrationData.objects.filter(mobile=mobile)
        if mob.exists():
            raise forms.ValidationError("Mobile number is already taken")
        elif len(str(mobile))!=10:
            raise forms.ValidationError("plz enter vaild mobile number")
        return  mobile
    def clean(self):
        data=self.cleaned_data
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password2 !=password1:
            raise forms.ValidationError("password must be match")
        elif len(password1)<=4 or len(password2)>=15:
            raise forms.ValidationError("password length must be greater than 4 and lessthan 15")
        return data





















