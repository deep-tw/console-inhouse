from django.shortcuts import render,HttpResponse, redirect
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .task import *

@login_required
def home(request):
    return redirect('login')


#User Registration
def registration(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        mobile_number=request.POST.get('mobile_number')
        password = request.POST.get('password')
        
        is_user_exists = User.objects.filter(email=email).exists()
 
        if is_user_exists:
            message= 'User with this email id already exists. Please proceed to login!!'
            return render(request, 'account/registration.html',{'message':message})

        print(username,email,mobile_number,password)
        user=User(username=username,email=email,mobile_number=mobile_number)
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request,'account/registration.html')

#User Login
def loginview(request):
    
    if request.method == 'POST':
        user_email=request.POST.get('email')
        user_password = request.POST.get('password')
      
  
       
        print(user_email,user_password)
        # users= User.objects.filter(email=user_email).exists()
        # if not users:
        #     message='Invalid Login Credentials!!'
        #     return render(request, 'account/login.html',{'messages':message})
        
        user= authenticate(username=user_email, password=user_password)
        print(user)
        if user is not None:
            login(request,user)
            get_user=User.objects.get(email=user_email)
            user_role=str(get_user.role)
            # print(type(user_role))
            # if user_role == 'Admin' :
            #     return redirect('admindashboard')
                
            # elif user_role == 'Manager':
                
            #     return redirect('managerdashboard')

            # elif user_role == 'Developer':

            #     return redirect('developerdashboard')
            # else:
            #     return render(request,'dashboard/userrole.html')
            return redirect("index")
        else:
            message='You entered invalid credential for Email.,password or you may not registered as a User!!'
            return render(request,'account/login.html',{'messages':message})

    return render(request, 'account/login.html')


def logoutview(request):
    logout(request)
    return redirect('login')


def change_password(request):
    role= str(request.user.role)
    if request.method == 'POST':
        old_password=request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')
        print(old_password,new_password,confirm_password)
        user=User.objects.get(username=request.user)
        if new_password == confirm_password :
            user.set_password(new_password)
            user.save()
            return redirect('login')
            # return render(request,'account/login.html',{'messages':'your password has been changed ,Please login'})
        else:
            return render(request,'account/change_password.html',{'messages':"new password and confirm password are not match"})

    return render(request,'account/change_password.html',locals())




list1= []
def send_mail_to_all(request):
    if request.method == 'POST':
        user_email=request.POST.get('email')
        is_user_exists = User.objects.filter(email=user_email).exists()
        if is_user_exists:
            send_mail_func.delay(user_email)
            user  = User.objects.filter(email = user_email)
            user_name =user[0]
            breakpoint()
            list1.append(user_name)
            return render(request, 'account/popup.html')
        
        else:
            message= 'This Email is not registered with us,Please provide Correct Email!!'
            return render(request, 'account/reset_password.html',{'message':message})
    return render(request,"account/reset_password.html")

            
def reset_password(request):
    if request.method == 'POST':
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        user_name=list1[0]
        if password1==password2:
            user_name.set_password(password1)
            user_name.save()
            return redirect('/account')
        else:
            message="Password mismatch"
            return render(request,"account/forgot_password.html",{'message':message})
    return render(request,"account/forgot_password.html")
        




    
           
            
            

