from pyexpat import model
from django import forms

from root.models import Donate_receipt
from .models import Join_us, Publication_pdf, Staff

class Staff_registrationForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name','dob','contact','email','speciality','role','work_details','about','picture']
        widgets={
                'name':forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Enter Fullname'}),
                'dob':forms.NumberInput(attrs={'class':'formDatePicker form-control flatpickr-input','type':'date','format':'%y-%m-%d'}),
                'role':forms.Select(attrs={'class':'form-select','type':'input'}),
                'email':forms.EmailInput(attrs={'class':'form-control input-height','type':'email','placeholder':'Enter Email'}),
                'contact':forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Enter Contact Number'}),
                'speciality':forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Ex. In AI/ML'}),
                'work_details':forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Ex. Associate Professor, Unitedworld School of Business,Gandhinagar, Gujarat, India'}),
                'about':forms.Textarea(attrs={'class':'form-control','type':'input','placeholder':'Enter details about yourself'}),
        
        
        }

class Join_usForm(forms.ModelForm): 
    class Meta: 
        model = Join_us 
        fields = ['name','adress','affiliation','email','contact','qualification','occupation','area_intrest_social','area_intrest_professional','brief_profile']
        widgets={
            'adress':forms.Textarea(attrs={'type':'input','placeholder':'Enter Your Address','rows':'7'}),
            'brief_profile':forms.Textarea(attrs={'type':'input','placeholder':'Enter Your Profile in brief','rows':'7'}),
            'name':forms.TextInput(attrs={'placeholder':'Enter Your name'}),
            'affiliation':forms.TextInput(attrs={'placeholder':'Enter Your affliation'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter Your Email'}),
            'contact':forms.TextInput(attrs={'placeholder':'Enter Your Contact Number'}),
            'qualification':forms.TextInput(attrs={'placeholder':'Enter Your Qualification'}),
            'occupation':forms.TextInput(attrs={'placeholder':'Enter Your Occupation'}),
            'area_intrest_social':forms.TextInput(attrs={'placeholder':'Enter Your Area of interest in social activites'}),
            'area_intrest_professional':forms.TextInput(attrs={'placeholder':'Enter Your Area of interest in Professional Services'}),
        }

class Publication_Form(forms.ModelForm):
    class Meta:
            model = Publication_pdf
            fields = ['title','file']
            widgets = {
                'title':forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Enter Title Of Publication'}),
            }

class Donate_receipt_Form(forms.ModelForm):
    class Meta:
            model = Donate_receipt
            fields = ['amount','received_date']
            widgets = {
                'amount':forms.TextInput(attrs={'class':'form-control input-height','type':'input','placeholder':'Enter Received amount'}),
                'received_date':forms.NumberInput(attrs={'class':'formDatePicker form-control flatpickr-input','type':'date','format':'%y-%m-%d'}),
            }