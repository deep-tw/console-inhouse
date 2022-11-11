from django.shortcuts import render,HttpResponse, redirect
from .models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, 'account/home.html')


def registration(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        mobile_number=request.POST['mobile_number']
        password = request.POST['password']
        
        is_user_exists = User.objects.filter(email=email).exists()
 
        if is_user_exists:
            message= 'User with this email id already exists. Please proceed to login!!'
            return render(request, 'account/registration.html',{'message':message})

        print(username,email,mobile_number,password)
        user=User(username=username,email=email,mobile_number=mobile_number)
        user.set_password(password)
        user.save()
        return render(request,'account/login.html')

    return render(request,'account/registration.html')


def login(request):
    
    if request.method == 'POST':
        user_email=request.POST['email']
        user_password = request.POST['password']
        try:
            users= User.objects.filter(email=user_email).exists()
            if not users:
                message='Invalid Login Credentials!!'
                return render(request, 'account/login.html',{'messages':message})

            get_user=User.objects.get(email=user_email)
            user_name=get_user.username
            user= authenticate(username=user_name, password=user_password)
            if user:

                return render(request,'account/home.html')
            else:
                message='You entered invalid credential for Email.,password or you may not registered as a User!!'
                return render(request,'account/login.html',{'messages':message})
        except:
            return render(request, 'account/login.html',{'messages':" please provide valid credentials "})

    return render(request, 'account/login.html')

def logoutview(request):
    logout(request)
    return redirect('login')





