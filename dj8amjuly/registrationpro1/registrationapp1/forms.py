from django import forms
from .models import ManishData

class ManishForm(forms.Form):
    class Meta:
        model=ManishData
        fields='__all__'

