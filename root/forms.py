from root.models import Doante_us, Mailbox
from django import forms

class Contact_Form(forms.ModelForm):
    class Meta:
        model = Mailbox
        fields = ['name','email','message','m_number']
        widgets= {
            'name':forms.TextInput(attrs={'placeholder':'Enter Your name'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter Your Email'}),
            'm_number':forms.TextInput(attrs={'placeholder':'Enter Your Contact Number'}),
            'message':forms.Textarea(attrs={'type':'input','placeholder':'Enter Your Message','rows':'10'}),
        }

class Donate_us_Form(forms.ModelForm): 
    class Meta: 
        model = Doante_us 
        fields = ['name','email','address','pan_no','transaction_detail','contact','date_ofdonation','entered_amount','donation_mode'] 
        widgets = { 
            'name' : forms.TextInput(attrs={'placeholder':'Enter Your Name'}), 
            'contact': forms.TextInput(attrs={'placeholder':'Enter Your Contact Number'}), 
            'date_ofdonation': forms.NumberInput(attrs={'class': 'form-control','type':'date'}),
            'entered_amount':forms.TextInput(attrs={'placeholder':'Enter Your Donation Amount','type':'number'}), 
            'donation_mode': forms.Select(attrs={'placeholder':'select donation mode'}),
            'email' : forms.TextInput(attrs={'placeholder':'Enter Your Email'}), 
            'address' : forms.Textarea(attrs={'type':'input','placeholder':'Enter Your Address','rows':'7'}), 
            'pan_no' : forms.TextInput(attrs={'placeholder':'Enter Your PAN Number'}), 
            'transaction_detail' : forms.Textarea(attrs={'type':'input','placeholder':'Enter Your Transaction Detail','rows':'7'}), 
        }