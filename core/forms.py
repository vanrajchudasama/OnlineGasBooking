from django import forms
from .models import Contact
class ContactForm(forms.Form):
    name=forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    email=forms.EmailField(label='Email Address',widget=forms.EmailInput(attrs={'class':'form-control form-control-sm'}))
    phone=forms.CharField(label='Contact No.',widget=forms.NumberInput(attrs={'class':'form-control form-control-sm'}))
    msg=forms.CharField(label='Massage',widget=forms.Textarea(attrs={'class':'form-control '}))
    
    class Meta:
        model=Contact
        fields='__all__'