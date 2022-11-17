from django.shortcuts import render, HttpResponseRedirect,redirect
from account.models import Project
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User
# Create your views here.
from django.utils import timezone
import logging

# Create your views here.
logger = logging.getLogger(__name__)
@login_required 
def index(request):
    # print(request.user.role, type(request.user.role))
    role= str(request.user.role)
    logger.error("Test!!")
    t = timezone.now()
    logging.debug("hello", t)
    return render (request, 'dashboard/index.html', locals())
    


def project(request):
    role= str(request.user.role)
    developers=User.objects.filter(role=3)
  
    try:
        user=request.user
        
        if request.method=="POST":
            project_name=request.POST.get('ProjectName')
            project_description=request.POST.get('description')
            project_reporting_manager=request.POST.get('ReportingManager')
            project_bde_manager=request.POST.get('BDEManager')
            project_start_date=request.POST.get('StartDate')
            project_closing_date =request.POST.get('ClosingDate')
            project_remark=request.POST.get('remark')
            project_status=request.POST.get('ProjectStatus')
            project_assignee=request.POST.get('cars')
            
            for x in developers:
                print(x.email,x.username,'###')

            projects = Project(
                project_name = project_name,
                project_description = project_description, 
                project_assignee = project_assignee,
                project_reporting_manager = project_reporting_manager,
                project_bde_manager = project_bde_manager,
                project_start_date = project_start_date,
                project_closing_date = project_closing_date,
                project_remark = project_remark,
                project_status = project_status
            )
            projects.save()
            return redirect('managerdashboard')

    except Exception as e:
        print(e)
    return render (request, 'dashboard/manager/project_create.html', {'developers':developers,'user':user,'role':role} )



# def show_data(request):
#         project_data = Project.objects.all()
#         return render(request, 'dashboard/index.html', {'project_data': project_data})



def delete_data(request, id):
    Project.objects.get(id=id).delete()
    return redirect('managerdashboard')


def update_data(request,id):
    user=request.user
    role= str(request.user.role)

    if request.method=="POST":
        project_name=request.POST.get('ProjectName')
        project_description=request.POST.get('description')
        project_reporting_manager=request.POST.get('ReportingManager')
        project_bde_manager=request.POST.get('BDEManager')
        project_start_date=request.POST.get('StartDate')
        project_closing_date =request.POST.get('ClosingDate')
        project_remark=request.POST.get('remark')
        project_status=request.POST.get('ProjectStatus')
    

        project_data = Project.objects.get(id=id)
        project_data.project_name = project_name
        project_data.project_description = project_description
        project_data.project_reporting_manager = project_reporting_manager
        project_data.project_bde_manager = project_bde_manager
        project_data.project_start_date = project_start_date
        project_data.project_closing_date = project_closing_date
        project_data.project_remark = project_remark
        project_data.project_status = project_status
        project_data.save()
        return redirect('managerdashboard')

    project = Project.objects.get(id=id)
    return render (request, 'dashboard/manager/project_update.html', {'role':role,'project_data':project})


    
