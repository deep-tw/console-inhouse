from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User,Project
from django.db.models import Prefetch


@login_required 
def managerdashboard(request):
    role= str(request.user.role)
    role= str(request.user.role)
    user_id=request.user.id
    developers=User.objects.filter(role=3).count()
    u=User.objects.filter(role=3)
    allprojects=Project.objects.all().count()
    dev=''
    for d in u:
        dev=d
    print(d.id,'88')
    status=request.user.status
    users1=Project.objects.prefetch_related(Prefetch('project_assignee',queryset=User.objects.filter(role=2)))
    for x in users1:
        print(x.__dict__)

    users=Project.objects.prefetch_related(Prefetch('project_assignee',queryset=User.objects.filter(role=3)))
    
    for x in users:
        print(x.__dict__)
        print(x.project_assignee_id,x.project_reporting_manager)
    print(users,'0000')
    projects=Project.objects.all()
    pro = Project.objects.select_related("project_assignee")
    
    return render (request,'dashboard/manager/managerhome.html',{'developers':developers,'role':role,'projects':projects,'allprojects':allprojects,'pro':pro})


def allprojects(request):
    projects=Project.objects.all()
    role= str(request.user.role)
    return render (request,'dashboard/manager/allProjects.html',locals())


def alldevelopers(request):
    role= str(request.user.role)
    # proj= Project.objects.get(project_name="Yurie").prefetch_related('project_assignee')
    # print(proj)
    # proj=Project.objects.filter(project_assignee__designation="Yurie")
    alldevelopers=User.objects.filter(role=3)
    return render (request, 'dashboard/manager/alldevelopers.html',locals())    

