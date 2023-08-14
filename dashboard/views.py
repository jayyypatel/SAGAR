from cmath import log
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from auth_system.models import CustomUser
from root.models import Doante_us, Donate_receipt, Mailbox
from pickle import FALSE
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dashboard.forms import Donate_receipt_Form, Publication_Form, Staff_registrationForm
from dashboard.models import Join_us, Publication_pdf, Staff
from .utils import Gen_pdf
from django.template.loader import get_template,render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from root.models import Mailbox
from django.db.models import Sum
###
from weasyprint import HTML
import os
# Create your views here.

@login_required(login_url='auth_system:login')
def index(request):
    user = CustomUser.objects.get(pk=request.user.id)
    join_members = Join_us.objects.filter(approved=True).count()
    pub_count = Publication_pdf.objects.all().count()
    con_count = Mailbox.objects.all().count()
    total_damount = Donate_receipt.objects.all().aggregate(Sum('amount'))
    d_count = Donate_receipt.objects.all().count()
    join_request_count = Join_us.objects.filter(approved=False).count()
    donateus_count = Doante_us.objects.filter(approve=False).count() 

    context = {
        'user':user,
        'join_members':join_members,
        'pub_count':pub_count,
        'con_count':con_count,
        'total_damount':total_damount['amount__sum'],
        'd_count':d_count,
        'join_request_count':join_request_count,
        'donateus_count':donateus_count
    }
    return render(request,'dashboard/index.html',context)

@login_required(login_url='auth_system:login')
def join_us_request(request):
    join_request = Join_us.objects.filter(approved = False)
    print(join_request)
    context={
        'join_request':join_request,
    }
    return render(request,'dashboard/join_us_request.html',context)

#! start here

@login_required(login_url='auth_system:login')
def approved_membership(request):
    members= Join_us.objects.filter(approved = True)

    context={
        'members':members
    }
    return render(request,'dashboard/approved_membership.html',context)

#for approve button click
@login_required(login_url='auth_system:login')
def approve_request(request,id):#join us request approved view
    member = Join_us.objects.get(pk=id)
    context = {
        'name':member.name,
        'date':datetime.now,
        'purpose':'Join Us',
        'purpose_details':'Please find the pdf attached in email'
    }
    template_render  = render_to_string('dashboard/tmp_join_pdf.html', context)
    pdf = HTML(string=template_render).write_pdf()
    e_tmp = 'dashboard/email_mastertmp.html'      #
    
    #?
    # email = EmailMessage(
    #     "Join Us Registration Certificate",
    #     content,
    #     settings.EMAIL_HOST_USER,
    #     [member.email]
    # )
    
    # email.content_subtype = "html"
    # email.attach("document.pdf", pdf,"application/pdf")
    # email.send()
    #?
    #current running
    #certificate number process
    year = datetime.now().year #2022
    month = datetime.now().month #8
    word = 'JOIN' 
    count = 1
    # print(combinations)
    latest_obj = Join_us.objects.latest('certificate_no')
    tmp = ''
    if latest_obj.certificate_no is not None:
        before_cut = latest_obj.certificate_no
        for i in before_cut[::-1]:
            
            if i == '/':
                break
            else:
                tmp += i #3001
        increment =  int(tmp[::-1])+1  #1003
        member.certificate_no = f'{word}/{year}/{month}/{increment}'#1004

    if latest_obj.certificate_no is None:
        member.certificate_no = f'{word}/{year}/{month}/{count}'
    #certificate number process end
    withoutpdf_tmp = 'dashboard/email_cum_member_certificate.html'
    data ={
        'name':member.name,
        'c_id':member.certificate_no,
    }
    content = render_to_string(withoutpdf_tmp,data)
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

    msg = EmailMessage("Join Us Registration Certificate", None,  settings.EMAIL_HOST_USER,  [member.email])
    msg.attach(html_part) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
    # msg.attach("document.pdf", pdf,"application/pdf")
    msg.send()
    #current running end
    #####################################
    #
    
    #
    member.approved = True
    member.save()
    return redirect('dashboard:approved_membership')

@login_required(login_url='auth_system:login')
def delete_request(request,id):
    member = Join_us.objects.get(pk=id)
    member.delete()
    return redirect('dashboard:join_us_request')



@login_required(login_url='auth_system:login')
def request_profile(request,id):
    profile = Join_us.objects.get(pk=id)

    context={
        'profile':profile
    }
    return render(request,'dashboard/request_profile.html',context)


@login_required(login_url='auth_system:login')
def publications(request):
    publications = Publication_pdf.objects.all()

    context={
        'all_pub':publications
    }
    return render(request,'dashboard/publications.html',context)


@login_required(login_url='auth_system:login')
def add_publications(request):
    if request.method == 'POST':
        form = Publication_Form(request.POST,request.FILES)   

        if form.is_valid():
            form.save()
            messages.success(request,'Publication added successfully.')
            return redirect('dashboard:publications')
    else:
        form = Publication_Form()
    context={
        'form':form
    }
    return render(request,'dashboard/add_publications.html',context)

@login_required(login_url='auth_system:login')
def delete_publications(request,id):
    obj = Publication_pdf.objects.get(pk=id)
    obj.delete()
    return redirect('dashboard:publications')

@login_required(login_url='auth_system:login')
def edit_publications(request,id):
    
    context={

    }
    return render(request,'dashboard/edit_publications.html',context)

@login_required(login_url='auth_system:login') 
def contact_us_request(request): 
    contact_request = Mailbox.objects.all()
    context={ 
        'contact_request':contact_request 
    } 
    return render(request,'dashboard/contact_us_request.html',context) 

@login_required(login_url='auth_system:login') 
def delete_contact_request(request,id): 
    obj = Mailbox.objects.get(pk=id) 
    obj.delete() 
    return redirect('dashboard:contact_us_request') 

@login_required(login_url='auth_system:login') 
def donate_us_request(request): 
    donate_request = Doante_us.objects.filter(approve = False) 

    context={ 
        'donate_request':donate_request 

    } 
    return render(request,'dashboard/donate_us_request.html',context)

@login_required(login_url='auth_system:login')
def donate_receipt(request,id):
    donate_obj = Doante_us.objects.get(pk=id)
    if request.method == 'POST':
        form = Donate_receipt_Form(request.POST)
        
        if form.is_valid():
            #email start here
            #30/7/2022 this is original pdf code working in offfline
            # data_pdf ={
            #     'name':donate_obj.name,
            #     'pan':donate_obj.pan_no,
            #     'received_date':request.POST['received_date'],
            #     'amount':request.POST['amount'],
            #     'email':donate_obj.email,
            #     'date':datetime.now,
            #     'purpose':'Donate Us',
            #     'purpose_details':'Your received donation will be used to help society'
    
            # }
            # template_render  = render_to_string('dashboard/donate_invoice_pdf.html', data_pdf)
            # pdf = HTML(string=template_render).write_pdf()
            # e_tmp = 'dashboard/email_mastertmp.html'
            # content = render_to_string(e_tmp,data_pdf)
            #30/7/2022
            #?
            # email = EmailMessage(
            #     "Donation Receipt From Sagar Foundation",#subject
            #     content,#body
            #     settings.EMAIL_HOST_USER,
            #     [donate_obj.email]
            # )
            # email.content_subtype = "html"
            # email.attach("donation_receipt.pdf", pdf,"application/pdf")
            # email.send()
            #?
            #30/7/2022 this is original pdf code working in offfline
            # img_data = open('static/images/logo_withoutbg.png', 'rb').read()
            # html_part = MIMEMultipart(_subtype='related')
            # body = MIMEText(content, _subtype='html')
            # html_part.attach(body)

            # # Now create the MIME container for the image
            # img = MIMEImage(img_data, 'png')
            # img.add_header('Content-Id', '<myimage>')  # angle brackets are important
            # img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            # # img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            # html_part.attach(img)

            # msg = EmailMessage("Donation Receipt From Sagar Foundation", None,  settings.EMAIL_HOST_USER,  [donate_obj.email])
            # msg.attach(html_part) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
            # msg.attach("donation_receipt.pdf", pdf,"application/pdf")
            # msg.send()
            #30/7/2022
            #####
            # e_tmp2 = 'dashboard/email_cum_donationreceipt.html'
            #certificate number process
            year = datetime.now().year #2022
            month = datetime.now().month #8
            word = 'DONATE' 
            count = 1
            # print(combinations)
            latest_obj = Doante_us.objects.latest('certificate_no')
            tmp = ''
            if latest_obj.certificate_no is not None:
                before_cut = latest_obj.certificate_no
                for i in before_cut[::-1]:
                    
                    if i == '/':
                        break
                    else:
                        tmp += i #3001
                increment =  int(tmp[::-1])+1  #1003
                donate_obj.certificate_no = f'{word}/{year}/{month}/{increment}'#1004

            if latest_obj.certificate_no is None:
                donate_obj.certificate_no = f'{word}/{year}/{month}/{count}'
            #certificate number process end

            e_tmp2 = 'dashboard/email_donation_receipt_sign.html'
            data_2 = {
                'name':donate_obj.name,
                'pan_no':donate_obj.pan_no,
                'r_id':donate_obj.certificate_no,
                'amount':request.POST['amount'],
                'address':donate_obj.address,
                'today':datetime.now,
                't_details':donate_obj.transaction_detail
            }
            tmp = get_template(e_tmp2)
            content = tmp.render(data_2)

            img_data = open('static/images/logo_withoutbg.png', 'rb').read()
            img_data2 = open('static/sign.png', 'rb').read()
            html_part = MIMEMultipart(_subtype='related')
            body = MIMEText(content, _subtype='html')
            html_part.attach(body)

            # Now create the MIME container for the image
            img = MIMEImage(img_data, 'png')
            img.add_header('Content-Id', '<myimage>')  # angle brackets are important
            img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            #for second image
            img2 = MIMEImage(img_data2, 'png')
            img2.add_header('Content-Id', '<sign>')  # angle brackets are important
            img2.add_header("Content-Disposition", "inline", filename="sign") # David Hess recommended this edit
            # img.add_header("Content-Disposition", "inline", filename="myimage") # David Hess recommended this edit
            html_part.attach(img)
            html_part.attach(img2)
            to_mail = donate_obj.email
            msg = EmailMessage("Donation Receipt From SAGAR Foundation", None,  settings.EMAIL_HOST_USER,  [to_mail])
            msg.attach(html_part) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
            msg.send()
            #email end here
            form = form.save(commit=False)
            form.donate_id = donate_obj
            form.save()
            donate_obj.approve = True
            donate_obj.save()

            return redirect('dashboard:donate_approved')
    else:
        form = Donate_receipt_Form()
    context ={
        'form':form
    }
    return render(request,'dashboard/donate_receipt.html',context)

@login_required(login_url='auth_system:login')
def donate_details(request,id):
    donate_obj = Doante_us.objects.get(pk=id)
    context = {
        'donate':donate_obj
    }
    return render(request,'dashboard/donate_details.html',context)

@login_required(login_url='auth_system:login')
def donate_approved(request):
    donate_receipt = Donate_receipt.objects.all()
    context ={
        'donate':donate_receipt
    }
    return render(request,'dashboard/donate_approved.html',context)

@login_required(login_url='auth_system:login')
def donate_delete(request,id):
    obj = Doante_us.objects.get(pk=id)
    obj.delete()
    return redirect('dashboard:donate_us_request')