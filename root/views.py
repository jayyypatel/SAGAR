from cgitb import html
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http import client
from multiprocessing import context
from this import d
from urllib import request
from django.shortcuts import render,redirect
from dashboard.forms import Join_usForm
from django.contrib import messages
from dashboard.models import Publication_pdf, Staff
import os
from django.templatetags.static import static
#

import json
from django.http import HttpResponse

#
#email
from django.core.mail import EmailMessage,send_mail,EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template,render_to_string
from django.conf import settings
from pathlib import Path
###########

#####
from root.forms import Contact_Form, Donate_us_Form
# Create your views here.
def index(request):
    context={

    }
    return render(request,'root/index.html',context)

# def error_404(request,exception):
#     response = render(request, 'auth_system/error_404.html')
#     response.status_code = 404
#     return response

# def error_500(request):
#     response = render(request, 'auth_system/error_404.html')
#     response.status_code = 500
#     return response
#for about us page
def aboutus(request):
    
    context = {

    }
    return render(request,'root/aboutus.html',context)

def announcement(request):

    return render(request,'root/announcement_tab.html')

def contact(request):
    
    if request.method == 'POST':
        
        form = Contact_Form(request.POST)

        clientKey= request.POST['g-recaptcha-response']
        secretKey= '6LdsE1ghAAAAAAQweLceMNy8vkjW0wgjGkd3Rp-y'
        captchaData ={
            'secret':secretKey,
            'response':clientKey
        }
        

        if form.is_valid():
            
            form.save()
            messages.success(request,'“Thank you for your interest in activities of “SAGAR Foundation. We will reach out to you shortly.”')
            #this email is used to send email to end-user
            #?this is main
            e_tmp = 'root/email_thank_contact.html'
            c = {'name':request.POST['name']}
            content = render_to_string(e_tmp,c)
            # email = EmailMessage(
            #     "Contact Us request received",
            #     content,
            #     settings.EMAIL_HOST_USER,
            #     [request.POST['email']]
            # )
            
            # email.content_subtype = "html"
            # email.send()
            # ?main ends here
            #!
            img_data = open('static/images/logo_withoutbg.png', 'rb').read()

            # Create a "related" message container that will hold the HTML 
            # message and the image. These are "related" (not "alternative")
            # because they are different, unique parts of the HTML message,
            # not alternative (html vs. plain text) views of the same content.
            html_part = MIMEMultipart(_subtype='related')

            # Create the body with HTML. Note that the image, since it is inline, is 
            # referenced with the URL cid:myimage... you should take care to make
            # "myimage" unique
            # body = MIMEText('<p>Hello <img src="cid:myimage" class="CToWUd"/></p>', _subtype='html')

            body = MIMEText(content, _subtype='html')
            html_part.attach(body)

            # Now create the MIME container for the image
            img = MIMEImage(img_data, 'png')
            img.add_header('Content-Id', '<myimage>')  # angle brackets are important
            # img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            html_part.attach(img)

            # Configure and send an EmailMessage
            # Note we are passing None for the body (the 2nd parameter). You could pass plain text
            # to create an alternative part for this message
            msg = EmailMessage("Contact Us request received", None,  settings.EMAIL_HOST_USER,  [request.POST['email']])
            msg.attach(html_part) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
            msg.send()
            #!
            #this email sended to admin email address
            html = MIMEMultipart(_subtype='related')
            e_tmp2 = 'dashboard/email_admin_contactus.html'
            data = {
                'name':request.POST['name'],
                'email':request.POST['email'],
                'm_data':request.POST['message'],
                'date':datetime.now
            }
            content = render_to_string(e_tmp2,data)
            body = MIMEText(content, _subtype='html')
            html.attach(body)
            img = MIMEImage(img_data, 'png')
            img.add_header('Content-Id', '<myimage>')  # angle brackets are important
            # img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            html.attach(img)
            email_admin = EmailMessage("Contact Us request received", None,  settings.EMAIL_HOST_USER,  [settings.EMAIL_HOST_USER])
            email_admin.attach(html)
            email_admin.send()
            #?
            # e_tmp2 = 'dashboard/email_admin_contactus.html'
            # data = {
            #     'name':request.POST['name'],
            #     'email':request.POST['email'],
            #     'm_data':request.POST['message'],
            #     'date':datetime.now
            # }
            # content = render_to_string(e_tmp2,data)
            # email = EmailMessage(
            #     "Contact Us request received",
            #     content,
            #     settings.EMAIL_HOST_USER,
            #     [settings.EMAIL_HOST_USER]
            # )
            
            # email.content_subtype = "html"
            # email.send()
            #?
            return redirect('root:contact')

    else:
        form = Contact_Form()

    context = {
        'form':form
    }
    return render(request,'root/contact.html',context)



def join_us(request):

    if request.method == 'POST':
        form = Join_usForm(request.POST)

        if form.is_valid():
            form.save()
            #?
            #email start here
            data ={
                'name':request.POST['name'],
                'purpose':'Join Us Request',
                'purpose_details':'Thank you for your interest in activities of SAGAR Foundation. You will get Membership Certificate on approval of your membership.'
            }
            e_tmp = 'dashboard/email_mastertmp.html'
            content = render_to_string(e_tmp,data)
            # email = EmailMessage(
            #     "Join Us request received",
            #     content,
            #     settings.EMAIL_HOST_USER,
            #     [request.POST['email']]
            # )

            # email.content_subtype = "html"
            # email.send()
            #?
            #!
            img_data = open('static/images/logo_withoutbg.png', 'rb').read()
            html_part = MIMEMultipart(_subtype='related')
            body = MIMEText(content, _subtype='html')
            html_part.attach(body)

            # Now create the MIME container for the image
            img = MIMEImage(img_data, 'png')
            img.add_header('Content-Id', '<myimage>')  # angle brackets are important
            img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            # img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            html_part.attach(img)

            msg = EmailMessage("Join Us request received", None,  settings.EMAIL_HOST_USER,  [request.POST['email']])
            msg.attach(html_part) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
            msg.send()
            #!
            #email ends here
            #?
            #this email for admin
            e_tmp2 = 'dashboard/email_admin_joindonate.html'
            data = {
                'name':request.POST['name'],
                'email':request.POST['email'],
                'date':datetime.now,
                'purpose':'Join Us Request'
            }
            content = render_to_string(e_tmp2,data)
            # email = EmailMessage(
            #     "Join Us Request received",
            #     content,
            #     settings.EMAIL_HOST_USER,
            #     [settings.EMAIL_HOST_USER]
            # )
            
            # email.content_subtype = "html"
            # email.send()
            #?
            #!
            html_part2 = MIMEMultipart(_subtype='related')
            body = MIMEText(content, _subtype='html')
            html_part2.attach(body)
            html_part2.attach(img)

            msg = EmailMessage("Join Us request received", None,  settings.EMAIL_HOST_USER,  [settings.EMAIL_HOST_USER])
            msg.attach(html_part2) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
            msg.send()
            #!
            messages.success(request,'Thank you for your interest in activities of SAGAR Foundation. You will get Membership Certificate on approval of your membership.')
            return redirect('root:join_us')
    else:
        form = Join_usForm() 
    context = { 
        'form':form 
    } 
    return render(request,'root/join_us.html',context)

def activities(request):
    
    
    context ={

    }
    return render(request,'root/activities.html',context)

def singleblog(request):

    context={

    }
    return render(request,'root/singleblog.html',context)

def events(request):

    context = {

    }
    return render(request,'root/events.html',context)

def social_contribution(request):

    context ={

    }
    return render(request,'root/social_contribution.html',context)

def publications(request):
    publications = Publication_pdf.objects.all()
    context ={
        'publications':publications
    }
    return render(request,'root/publications.html',context)

def donate_us(request): 
    if request.method == 'POST': 
        form = Donate_us_Form(request.POST) 

        if form.is_valid(): 
            form.save()
            data ={
                'name':request.POST['name'],
                'purpose_details':'“ Thank you for your kind support in activities of SAGAR Foundation. Donation Receipt will be share with you shortly”'
            }
            e_tmp = 'dashboard/email_mastertmp.html'
            content = render_to_string(e_tmp,data).strip()
            #?
            # email = EmailMessage(
            #     "Donation receipt request",
            #     content,
            #     settings.EMAIL_HOST_USER,
            #     [request.POST['email']]
            # )

            # email.content_subtype = "html"
            # email.send()
            #?
            #!
            img_data = open('static/images/logo_withoutbg.png', 'rb').read()
            html_part = MIMEMultipart(_subtype='related')
            body = MIMEText(content, _subtype='html')
            html_part.attach(body)

            # Now create the MIME container for the image
            img = MIMEImage(img_data, 'png')
            img.add_header('Content-Id', '<myimage>')  # angle brackets are important
            img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            # img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            html_part.attach(img)

            msg = EmailMessage("Donation receipt request", None,  settings.EMAIL_HOST_USER,  [request.POST['email']])
            msg.attach(html_part) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
            msg.send()
            
            #!
            #this email for admin
            #?
            e_tmp2 = 'dashboard/email_admin_joindonate.html'
            data = {
                'name':request.POST['name'],
                'email':request.POST['email'],
                'date':datetime.now,
                'purpose':'Donate Us Request'
            }
            content2 = render_to_string(e_tmp2,data)
            # email = EmailMessage(
            #     "Donate Us Request received",
            #     content,
            #     settings.EMAIL_HOST_USER,
            #     [settings.EMAIL_HOST_USER]
            # )
            
            # email.content_subtype = "html"
            # email.send()
            #?
            #!
            html_part2 = MIMEMultipart(_subtype='related')
            body = MIMEText(content2, _subtype='html')
            html_part2.attach(body)
            html_part2.attach(img)

            msg = EmailMessage("Donate Us request received", None,  settings.EMAIL_HOST_USER,  [settings.EMAIL_HOST_USER])
            msg.attach(html_part2) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
            msg.send()
            #!
            messages.success(request,'Thank you for your kind support in activities of SAGAR Foundation. Donation Receipt will be share with you on your registered email ID.') 
            return redirect('root:donate_us') 

    else: 
        form = Donate_us_Form() 

    context ={ 
        'form':form 

    } 
    return render(request,'root/donate_us.html',context)

#social contributions
def social_1(request):#Empowerment of Persons
    return render(request,'root/social_1.html')

def social_2(request): #Women Empowerment 
    return render(request,'root/social_2.html') 

def social_2_jamnagar(request): #Tailoring and Cutting Training at Jamanagar
    return render(request,'root/social_2_jamnagar.html') 

def social_3(request): #Self Help Group 
    return render(request,'root/social_3.html') 

def social_4(request): #Self Employment Training 
    return render(request,'root/social_4.html') 

def social_5(request): #Education for All 
    return render(request,'root/social_5.html') 

def social_6(request): #AIDS Awareness 
    return render(request,'root/social_6.html') 

def social_7(request): #Legal Aid 
    return render(request,'root/social_7.html') 

def social_8(request): #Rural Development Program 
    return render(request,'root/social_8.html') 

def social_9(request): #Computer literacy and awareness 
    return render(request,'root/social_9.html') 

def social_10(request): #Safe Drinking Water for All 
    return render(request,'root/social_10.html') 

def social_11(request): #Non Conventional Energy 
    return render(request,'root/social_11.html') 

def social_12(request): #Children Rights and Child Protection 
    return render(request,'root/social_12.html') 

def social_13(request): #Micro Finance 
    return render(request,'root/social_13.html') 

def social_14(request): #Environmental Protection and Sustainable Development 
    return render(request,'root/social_14.html')

#Professional Activities
def professional_activities(request):
    return render(request,'root/prof_activities.html')

def prof_1(request):#Research Counseling
    return render(request,'root/prof_1.html')

def prof_2(request):#Data analysis
    return render(request,'root/prof_2.html')

def prof_3(request):#Application of Computer for Research
    return render(request,'root/prof_3.html')

def prof_4(request):#Research methods and methodology Report Writing
    return render(request,'root/prof_4.html')

def prof_5(request):#Communication Training
    return render(request,'root/prof_5.html')

def prof_6(request):#Corporate Communication
    return render(request,'root/prof_6.html')
    
def prof_7(request):#Content development
    return render(request,'root/prof_7.html')

def prof_8(request):#Financial advisory
    return render(request,'root/prof_8.html')

def prof_9(request): #Market Research 
    return render(request,'root/prof_9.html') 

def prof_10(request): #Doctoral Counseling 
    return render(request,'root/prof_10.html') 

def prof_11(request): #Research publication 
    return render(request,'root/prof_11.html') 

def prof_12(request): #Career Counseling 
    return render(request,'root/prof_12.html') 

def prof_13(request): #Personal Counseling 
    return render(request,'root/prof_13.html') 

def prof_14(request): #Psychological Counseling 
    return render(request,'root/prof_14.html') 

def prof_15(request): #Corporate Counseling 
    return render(request,'root/prof_15.html') 

def prof_16(request): #Family Counseling 
    return render(request,'root/prof_16.html') 

def prof_17(request): #Web Designing 
    return render(request,'root/prof_17.html') 

def prof_18(request): #Digital Marketing 
    return render(request,'root/prof_18.html')

def email(request):
    e_tmp2 = 'dashboard/email_cum_member_certificate.html'
    data = {
                'name':'Jay Patel',
                'c_id':'15',
            }
    tmp = get_template(e_tmp2)
    content = tmp.render(data)


    img_data = open('static/images/logo_withoutbg.png', 'rb').read()
    html_part = MIMEMultipart(_subtype='related')
    body = MIMEText(content, _subtype='html')
    html_part.attach(body)

    # Now create the MIME container for the image
    img = MIMEImage(img_data, 'png')
    img.add_header('Content-Id', '<myimage>')  # angle brackets are important
    img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
    # img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
    html_part.attach(img)
    to_mail = 'unicornwebworld@gmail.com'
    msg = EmailMessage("Membership Certificate From Sagar Foundation", None,  settings.EMAIL_HOST_USER,  [to_mail])
    msg.attach(html_part) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
    msg.send()
