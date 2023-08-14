from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class RegisterUser_form(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','contact','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Enter Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Enter Last Name'}),
            'contact': forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Enter Contact'}),
            'email': forms.TextInput(attrs={'class':'form-control input-height','type':'email','placeholder':'Enter Email'}),
            'password1': forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input-height','placeholder':'Enter Password'})),
            # 'password2': forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Confirm Password'}),
        }

class LoginUser_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-height','placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-height','placeholder': 'Password'}))