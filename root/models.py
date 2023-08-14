from django.db import models
from django.utils import timezone


class Mailbox(models.Model):#contact_us
    email = models.EmailField(blank=False)
    message = models.CharField(max_length=500,blank=False)
    name = models.CharField(max_length=150,blank=False)
    m_number = models.CharField(max_length=13,null=True)#####new field
    date = models.DateField(default=timezone.now)
 
mode = (
    ('cash','Cash'),
    ('bank_transfer','Bank Transfer'),
    ('cheque','Cheque'),
    ('other','Other'),
)

class Doante_us(models.Model): 
    name = models.CharField(max_length=100,blank=False) 
    email = models.EmailField(blank=False) 
    address = models.CharField(max_length=800,blank=False) 
    pan_no = models.CharField(max_length=20,blank=False) 
    transaction_detail = models.CharField(max_length=800,blank=False) 
    approve = models.BooleanField(default=False)#false = not approved and true approved 
    #new added items after update
    contact = models.CharField(max_length=13,null=True,blank=False)
    date_ofdonation = models.DateField(default=timezone.now,null=True,blank=False)
    entered_amount = models.IntegerField(null=True,blank=False)
    donation_mode = models.CharField(choices=mode,blank=False,max_length=15,null=True)
    certificate_no = models.CharField(max_length=30,null=True,blank=True)


    def __str__(self):  
        return f'{self.name}  --  {self.certificate_no}'

class Donate_receipt(models.Model):
    amount = models.IntegerField()
    received_date = models.DateField(timezone.now)
    donate_id = models.ForeignKey(Doante_us,on_delete=models.CASCADE,related_name='donate_receipt')

    def __str__(self):
        return f'{self.amount}'