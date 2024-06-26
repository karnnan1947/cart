from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import customer
from products.models import Product
# Create your views here.
def signout(request):
    logout(request)
    return redirect('index')

def account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:    
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phonenumber=request.POST.get('phonenumber')
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            customers=customer.objects.create(
                user=user,
                name=username,
                address=address,
                phone=phonenumber)
            messages.success(request,"registration success")
        except Exception as e:
            error_message="duplicate error"
            messages.error(request,"duplicate error")
    else:        
        if request.POST and 'login' in request.POST:
            context['login']=False
            username=request.POST['username']
            password=request.POST['password']
            print(username,password)
            user=authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request,"invalid details")
    return render(request,'account.html',context)


