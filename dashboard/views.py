from django.shortcuts import render, HttpResponseRedirect,redirect
from account.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render (request, 'dashboard/index.html',  {"project_data": projects})



def project(request):

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
            
            projects = Project(
                project_name = project_name,
                project_description = project_description, 
                project_assignee = user,
                project_reporting_manager = project_reporting_manager,
                project_bde_manager = project_bde_manager,
                project_start_date = project_start_date,
                project_closing_date = project_closing_date,
                project_remark = project_remark,
                project_status = project_status
            )
            projects.save()
            return redirect('/')

    except Exception as e:
        print(e)
    return render (request, 'projects/project_create.html', {'user':user} )



# def show_data(request):
#         project_data = Project.objects.all()
#         return render(request, 'dashboard/index.html', {'project_data': project_data})



def delete_data(request, id):
    Project.objects.get(id=id).delete()
    return redirect('/')


def update_data(request,id):
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
        return HttpResponseRedirect('/')

    project = Project.objects.get(id=id)
    return render (request, 'projects/project_update.html', {'project_data':project})

