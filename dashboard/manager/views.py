from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User,Project

@login_required 
def managerdashboard(request):
    role= str(request.user.role)
    user_id=request.user.id
    status=request.user.status

    users=User.objects.filter(role=request.user.role)
    for x in users:
        print(x.id,x.email,x.username,x.status)
    projects=Project.objects.all()
    print(users,status,projects)

    return render (request,'dashboard/manager/managerhome.html',{'role':role,'projects':projects})

def allprojects(request):
    projects=Project.objects.all()
    role= str(request.user.role)

    return render (request,'dashboard/manager/projects.html',{'role':role,'projects':projects})

