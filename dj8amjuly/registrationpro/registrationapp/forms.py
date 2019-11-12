from django import forms

class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="Enter your first name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your first_name is:'
            }
        )
    )
    last_name=forms.CharField(
        label="Enter your last name;",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your last_name is:'
            }
        )
    )
    username=forms.CharField(
        label="Enter User name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username is:'
            }
        )
    )
    password=forms.CharField(
        label="your password is:",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'password is:'
            }
        )
    )
    email=forms.EmailField(
        label="your email is:",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'email is:'
            }
        )
    )
    mobile=forms.IntegerField(
        label="your mobile is:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile is:'
            }
        )
    )

class LoginForm(forms.Form):
    username=forms.CharField(
        label="your username is:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your username is:'
            }
        )
    )
    password=forms.CharField(
        label="your password is:",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your password is'
            }
        )
    )
