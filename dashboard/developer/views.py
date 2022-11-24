from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Project,ProjectAssign,Rating
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

