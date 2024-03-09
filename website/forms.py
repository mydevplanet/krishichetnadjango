# forms.py
from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
                            max_length=100
                            )
    email = forms.EmailField(
         widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=200)
    message = forms.CharField(
         widget=forms.Textarea(attrs={'class': 'form-control'}),
        )

