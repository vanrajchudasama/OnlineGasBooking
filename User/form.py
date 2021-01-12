from django import forms
from .models import Users,Connection
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm

class UserForm(UserCreationForm):
    
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'id':'fname','class':'form-control','autofocus':True}))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'id':'lname','class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'id':'email','class':'form-control','required': False}))
    
    #  mobile = forms.CharField(label='Mobile',widget=forms.NumberInput(attrs={'id':'mobile','class':'form-control'}))
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'id':'id_username','autofocus':False,'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'id':'password1','class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'id':'password2','class':'form-control'}))
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username)<11:
            raise forms.ValidationError('This username is too short. It must contain at least 10 characters.')
        return username
    def clean_email(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this Email already exists.")
       return email
    
    class Meta:
        model=User
        fields = ('first_name','last_name','email','username','password1','password2')
    
class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'id':'fname','class':'form-control','autofocus':True}))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'id':'lname','class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'id':'email','class':'form-control','required': False}))
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'id':'id_username','autofocus':False,'class':'form-control'}))
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username)<11:
            raise forms.ValidationError('This username is too short. It must contain at least 10 characters.')
        return username
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
class ProfileForm(forms.ModelForm):
    mobile = forms.CharField(label='Mobile',widget=forms.NumberInput(attrs={'id':'mobile','class':'form-control'}))
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(mobile)!=10:
            raise forms.ValidationError('enter valid mobile number')
        if Users.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError("User with this Mobile already exists.")
        return mobile
    
    class Meta:
        model=Users
        fields=('mobile',)
class ProfileUpdateForm(forms.ModelForm):
    mobile = forms.CharField(label='Mobile',widget=forms.NumberInput(attrs={'id':'mobile','class':'form-control'}))
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(mobile)!=10:
            raise forms.ValidationError('enter valid mobile number')
        
        return mobile
    class Meta:
        model=Users
        fields=('mobile',)
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'id':'username','class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'id':'pass','class':'form-control'}))
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(mobile)!=10:
            raise forms.ValidationError('enter valid mobile number')
        return mobile
class ChangepasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='New Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
