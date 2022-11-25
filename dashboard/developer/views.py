from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import Project,User
# Create your views here.
@login_required 
def developerdashboard(request):
    role= str(request.user.role)
    assignprojects=Project.objects.filter(project_assignee=request.user)  
    print(assignprojects)
    return render (request,'dashboard/developer/developerhome.html',locals())

def assignprojects(request):
    assignproject=Project.objects.filter(project_assignee=request.user)  
    for projects in assignproject:
         unassigned=User.objects.all().exclude(username=projects.project_assignee)
         print(unassigned.__dict__)
    role= str(request.user.role)
    return render (request,'dashboard/developer/assignprojects.html',locals())

def self_update_developer(request,id):
        role= str(request.user.role)
        if request.method=="POST":
                mobile_number=request.POST['mobile_number']
                username=request.POST['username']
                status=request.POST['status']
                technologies=request.POST['technologies']
                obj=User.objects.get(id=id)
                obj.mobile_number=mobile_number
                obj.username=username
                obj.status=status
                obj.technologies=technologies
                obj.save()
                return redirect('/developerdashboard/')
        developers=User.objects.get(id=id)
        return render(request,'dashboard/developer/self_update_developer.html',{'developer':developers,'role':role})    
