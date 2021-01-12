from django import forms
from .models import Connection,Address,Document
from django.contrib.auth.models import User

class ConnectionForm(forms.ModelForm):
    genders=[
        ('male','Male'),
        ('female','Female')
    ]
    relatives=[
        ('father','Father'),
        ('spouse','Spouse'),
    ]
    cylinder_choice= (
        ('14.2','14.2 Kg'),
        ('5','5Kg')
    )
    dob = forms.DateField(label='Date of Birth',widget=forms.DateInput(attrs={'class':'form-control','min':'1985-01-01','max':'2000-01-01'}))
    gender = forms.CharField(label='Gender',widget=forms.RadioSelect(attrs={'class':'form-control'},choices=genders))
    ffname = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    fmname = forms.CharField(label='Middle Name',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    flname = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
   
    mfname = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    mmname = forms.CharField(label='Middle Name',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    mlname = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    relative = forms.CharField(label='Relative',widget=forms.RadioSelect(attrs={'class':'form-control'},choices=relatives))
    
    
    class Meta:
        model = Connection
        fields=('gender','dob')
class AddressForm(forms.ModelForm):
    city = forms.CharField(label='City/Town/Village',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    district = forms.CharField(label='District',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))

    state = forms.CharField(label='State',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    pincode = forms.CharField(label='Pincode',widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','max':'6'}))
    country = forms.CharField(label='Country',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    address = forms.CharField(label='Address',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    def clean_pincode(self):
        pincode = self.cleaned_data['pincode']
        if len(pincode)!=6:
            raise forms.ValidationError('Enter valid pincode')
        return pincode
    class Meta:
        model=Address
        fields=('city','district','state','pincode','country','address')
    
class DocumentForm(forms.ModelForm):
    # user = forms.OneToOneField(User,on_delete=models.CASCADE)
    aadhar_no = forms.CharField(label='Aadhar No.',widget=forms.NumberInput(attrs={'class':'form-control form-control-sm'}))
    aadhar_image = forms.ImageField(label='Aadharcard',widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))
    rationcard_no = forms.CharField(label='Rationcard No.',widget=forms.NumberInput(attrs={'class':'form-control form-control-sm'}))
    rationcard_image = forms.ImageField(label='Rationcard',widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))
    def clean_aadhar_no(self):
        aadhar_no = self.cleaned_data.get('aadhar_no')
        if len(aadhar_no)!=12:
            raise forms.ValidationError('Enter valid Aadhar number')
        return aadhar_no
    def clean_aadhar_image(self):
        aadhar_image=self.cleaned_data.get('aadhar_image')
        filesize = aadhar_image.size
        kb=50.0
        if filesize>kb*1024:
            raise forms.ValidationError('Please enter < 50kb image')
        return aadhar_image
    def clean_rationcard_image(self):
        rationcard_image=self.cleaned_data.get('rationcard_image')
        filesize = rationcard_image.size
        kb=50.0
        if filesize>kb*1024:
            raise forms.ValidationError('Please enter < 50kb image')
        return rationcard_image
    class Meta:
        model=Document
        fields = ('aadhar_no','aadhar_image','rationcard_no','rationcard_image')