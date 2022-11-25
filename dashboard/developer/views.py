from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import Project,ProjectAssign,Rating,User
# Create your views here.


@login_required 
def developerdashboard(request):
    role= str(request.user.role)
    assignprojects=ProjectAssign.objects.filter(project_assignee=request.user).count() 
    rating_flag=True
    try:
        ratings=Rating.objects.get(developer_name=request.user)
    except:
        rating_flag=False
        return render(request,'dashboard/developer/developerhome.html',locals())

    return render(request,'dashboard/developer/developerhome.html',locals())


def assignprojects(request):
    assignproject=ProjectAssign.objects.filter(project_assignee=request.user) 
    print(assignproject)
    role= str(request.user.role)

    return render(request,'dashboard/developer/assignprojects.html',locals())

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
