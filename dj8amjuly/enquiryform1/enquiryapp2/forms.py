from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label="Enetr your name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name is'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobile is:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your mobile is:'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your Email is:",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email is:'
            }
        )
    )
    Gender_choices=(
        ('F','Female'),
        ('M','Male')
    )
    gender=forms.ChoiceField(
    widget=forms.RadioSelect,choices=Gender_choices
    )

    COURSES_CHOICES = (
        ('PY', 'PYTHON'),
        ('Dj', 'Django'),
        ('RA', 'Rest API'),
        ('Ui', 'UI')
    )
    courses = MultiSelectFormField(choices=COURSES_CHOICES)

    SHIFT_CHOICE = (
        ('Morning', 'Morning Shift'),
        ('Afternoon', 'Afternoon Shift'),
        ('Evening', 'Evening Shift'),
        ('Night', 'Night Shift')
    )
    shifts = MultiSelectFormField(choices=SHIFT_CHOICE)

    start_date = forms.DateTimeField(
        widget=forms.SelectDateWidget()
    )


