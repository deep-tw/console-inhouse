from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
# from account.models import User,Project,ProjectAssign,Rating


@login_required 
def managerdashboard(request):
    role= str(request.user.role)
    # print(str(request.user.role.id))
    user_id=request.user.id
    
    status=request.user.status
    users=User.objects.filter(role=request.user.role)
    # for x in users:
    #     print(x.id,x.email,x.username,x.status)
    # projects=Project.objects.all().count()
    projects=ProjectAssign.objects.filter(project_reporting_manager=request.user).count()
    developers=User.objects.filter(role=3).count()

    return render (request,'dashboard/manager/managerhome.html',locals())


# List of all Projects
def allprojects(request):
    # projects=Project.objects.all()
    manager=ProjectAssign.objects.filter(project_reporting_manager=request.user)
    role= str(request.user.role)
    return render (request,'dashboard/manager/allProjects.html',locals())


# List of all Developers
def alldevelopers(request):

    role= str(request.user.role)
    # proj= Project.objects.get(project_name="Yurie").prefetch_related('project_assignee')
    # print(proj)
    # proj=Project.objects.filter(project_assignee__designation="Yurie")
    alldevelopers=User.objects.filter(role=User.DEVELOPER)

    # for dev in alldevelopers:
    #     if Project.objects.filter(project_assignee=dev) and Project.objects.filter(project_reporting_manager=request.user):
    #         print(dev)

    # devl=[ProjectAssign.objects.filter(project_assignee=dev) for dev in alldevelopers]
    # print(devl,'&&&')
    
    return render (request, 'dashboard/manager/alldevelopers.html',locals())    

#Update Developer
def update_developer(request,id):
        role= str(request.user.role)
        if request.method=="POST":
                mobile_number=request.POST['mobile_number']
                designation=request.POST['designation']
                status=request.POST['status']
                technologies=request.POST['technologies']
                obj=User.objects.get(id=id)
                obj.mobile_number=mobile_number
                obj.designation=designation
                obj.status=status
                obj.technologies=technologies
                print(designation,"$$$$$$$$$$$$")
                obj.save()
                return redirect('/alldevelopers/')
        developers=User.objects.get(id=id)
        # breakpoint()  
        print(developers,"FFFFFFFFFFFFFFFFFFFFffff")
        print(developers.designation)
        return render(request,'dashboard/manager/update_developer.html',{'developers':developers,'role':role})

# # update Developer
# def update_developer(request,id):
#         role= str(request.user.role)
#         if request.method=="POST":
#                 mobile_number=request.POST['mobile_number']
#                 designation=request.POST['designation']
#                 status=request.POST['status']
#                 technologies=request.POST['technologies']
#                 obj=User.objects.get(id=id)
#                 obj.mobile_number=mobile_number
#                 obj.designation=designation
#                 obj.status=status
#                 obj.technologies=technologies
#                 obj.save()
#                 return redirect('/alldevelopers/')
#         developers=User.objects.get(id=id)
#         print(developers,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
#         # breakpoint()
#         return render(request,'dashboard/manager/update_developer.html',{'developer':developers,'role':role})

# Delete Developer
def delete_developer(request,id):
    developers=User.objects.get(id=id)
    developers.delete()
    return redirect('/alldevelopers/')



def allratings(request):
    role= str(request.user.role)
    ratings=Rating.objects.all()

    return render(request,'dashboard/manager/allratings.html',locals())

