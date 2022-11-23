from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Project,ProjectAssign
# Create your views here.
@login_required 
def developerdashboard(request):
    role= str(request.user.role)
    assignprojects=ProjectAssign.objects.filter(project_assignee=request.user).count() 
    print(assignprojects)
    return render(request,'dashboard/developer/developerhome.html',locals())

def assignprojects(request):
    assignproject=ProjectAssign.objects.filter(project_assignee=request.user) 
    print(assignproject)
    role= str(request.user.role)

    return render(request,'dashboard/developer/assignprojects.html',locals())