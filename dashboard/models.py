from datetime import datetime
from email.policy import default
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# Create your models here.

role_choice = (
    ('member','Member'),
    ('editor','Editor')
)
class Staff(models.Model):
    name = models.CharField(max_length=50,blank=False)
    dob = models.DateField(default=timezone.now)
    contact = models.CharField(max_length=15,blank=False)
    email = models.EmailField(blank=False)
    speciality = models.CharField(max_length=50,blank=False) 
    role = models.CharField(max_length=20,choices=role_choice,default='member')
    work_details = models.CharField(max_length=200,blank=False)#ex. designation and Work place and area 
    about = models.CharField(max_length=1000,blank=False) #more details
    picture = models.ImageField(upload_to='images',blank=False)

    def __str__(self):
        return f'{self.name}'

    def get_staff_img_url(self):
        return f"{self.picture.url}"

    
class Join_us(models.Model): 
    name = models.CharField(max_length=50,blank=False) 
    adress = models.CharField(max_length=100,blank=False) 
    affiliation = models.CharField(max_length=100,blank=False) 
    email = models.EmailField(blank=False) 
    contact = models.CharField(max_length=15,blank=False) 
    qualification = models.CharField(max_length=100,blank=False) 
    occupation = models.CharField(max_length=100,blank=False) 
    area_intrest_social = models.CharField(max_length=150,blank=True)#(SOCIAL CONTRIBUTION ACTIVITIES) 
    area_intrest_professional = models.CharField(max_length=150,blank=True) #(PROFESSIONAL SERVICES)
    brief_profile = models.CharField(max_length=400,blank=False) 
    approved = models.BooleanField(default=False)#false = not approved and true approved
    certificate_no = models.CharField(max_length=30,null=True,blank=True)


    def __str__(self): 
        return f'{self.name} -- {self.certificate_no}'

class Publication_pdf(models.Model):
    title = models.CharField(max_length=100,blank=False)#
    file = models.FileField(upload_to='pdfs',blank=False,validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    def __str__(self):
        return f'{self.title}'

