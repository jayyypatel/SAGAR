from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from auth_system.forms import LoginUser_form, RegisterUser_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    #pass this form to html page
    form = RegisterUser_form()
    if request.method == 'POST':
        form = RegisterUser_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('auth_system:login')

    context ={
        'form':form
    }
    return render(request,'auth_system/register.html',context)

def login(request):
    form = LoginUser_form()
    
    if request.method == 'POST':
        
        form = LoginUser_form(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request,username = username,password = password)
            
        if user_auth is not None:
            auth_login(request,user_auth)
            return redirect('dashboard:index')
        else:
            messages.error(request,'Username or Password not correct')
            
                
    context ={
            'form':form,
            
    }
    return render(request,'auth_system/login.html',context)

@login_required(login_url='auth_system:login')
def logout_user(request):

    logout(request)

    return redirect('auth_system:login')


def forgot_password(request):

    context ={

    }
    return render(request,'auth_system/forgot_password.html',context)