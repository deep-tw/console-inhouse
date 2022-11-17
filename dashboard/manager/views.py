from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User,Project

@login_required 
def managerdashboard(request):
    role= str(request.user.role)
    role= str(request.user.role)
    print(str(request.user.role.id))
    user_id=request.user.id
    developers=User.objects.filter(role=3).count()

    status=request.user.status
    users=User.objects.filter(role=request.user.role)
    for x in users:
        print(x.id,x.email,x.username,x.status)
    projects=Project.objects.all()
    print(users,status,projects)
    return render (request,'dashboard/manager/managerhome.html',{'developers':developers,'role':role,'projects':projects})

def allprojects(request):
    projects=Project.objects.all()
    role= str(request.user.role)
    
    return render (request,'dashboard/manager/projects.html',locals())


