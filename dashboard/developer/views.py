from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Project
# Create your views here.
@login_required 
def developerdashboard(request):
    role= str(request.user.role)

    return render (request,'dashboard/developer/developerhome.html',locals())

def assignprojects(request):
    # projects=Project.objects.all()
    assignprojects=Project.objects.filter(project_assignee=request.user)  
    print(assignprojects)
    role= str(request.user.role)

    return render (request,'dashboard/developer/assignprojects.html',locals())