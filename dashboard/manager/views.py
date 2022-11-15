from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User,Project

@login_required 
def managerdashboard(request):
    role= str(request.user.role)
    users=User.objects.get(email=request.user.email)
    projects=Project.objects.all()
    print(users,projects)
    
    return render (request,'dashboard/manager/managerhome.html',locals())

def alldevelopers(request):

    return render (request,'dashboard/manager/alldevelopers.html')

