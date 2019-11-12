from django import forms

class InsertingData(forms.Form):
    product_id=forms.IntegerField(
        label='Enter your Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product_ID'
            }
        )
    )
    product_name=forms.CharField(
        label='Enter your ProductName:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product_Name'
            }
        )
    )
    product_class=forms.CharField(
        label='Enter your product class:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product_Class'
            }
        )
    )
    product_color=forms.CharField(
        label='Enter Your Product Color:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    product_cost=forms.IntegerField(
        label='Enter your product cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product_Cost'
            }
        )
    )

class UpdatingData(forms.Form):
    product_id = forms.IntegerField(
        label='Enter your Product ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product_ID'
            }
        )
    )

    product_cost = forms.IntegerField(
        label='Enter your product cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product_Cost'
            }
        )
    )
class DeletingData(forms.Form):
    product_id = forms.IntegerField(
        label='Enter your Product ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product_ID'
            }
        )
    )







