from django import forms
from multiselectfield import MultiSelectField

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name is:'
            }
        )

    )
    email=forms.EmailField(
        label="Enter your email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email is'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobile",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile Number'
            }
        )
    )
    Gender_Choices=(
        ('F','Female'),
        ('M','Male')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect,choices=Gender_Choices
    )
    COURSES_CHOICES=(
        ('PY','PYTHON'),
        ('dj','Django'),
        ('rpi','RestAPI'),
        ('UI','UI')
    )
    courses=MultiSelectField(choices=COURSES_CHOICES)
    SHIFTS_CHOICES=(
        ('Morning','MorningShift'),
        ('Afternoon','Afternoonshift'),
        ('evening','Eveningshift'),
        ('night','NightShifts')
    )
    shifts=MultiSelectField(choices=SHIFTS_CHOICES)
    start_date=forms.DateTimeField(
        widget=forms.SelectDateWidget
    )




