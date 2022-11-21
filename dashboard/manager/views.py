from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from account.models import User,Project

@login_required 
def managerdashboard(request):
    role= str(request.user.role)
    role= str(request.user.role)
    # print(str(request.user.role.id))
    user_id=request.user.id
    developers=User.objects.filter(role=3).count()
    

    status=request.user.status
    users=User.objects.filter(role=request.user.role)
    # for x in users:
    #     print(x.id,x.email,x.username,x.status)
    projects=Project.objects.all().count()
    # print(users,status,projects)
    return render (request,'dashboard/manager/managerhome.html',{'developers':developers,'role':role,'projects':projects})

# List of all Projects
def allprojects(request):
    projects=Project.objects.all()
    role= str(request.user.role)
    return render (request,'dashboard/manager/allProjects.html',locals())

# List of all Developers
def alldevelopers(request):
    role= str(request.user.role)
    print(role)
    alldevelopers=User.objects.filter(role=3)

    print(alldevelopers)
    return render (request, 'dashboard/manager/alldevelopers.html',locals())  

# update Developer
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
                obj.save()
                return redirect('/alldevelopers/')
        developers=User.objects.get(id=id)
        print(developers,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        # breakpoint()
        return render(request,'dashboard/manager/update_developer.html',{'developer':developers,'role':role})

# Delete Developer
def delete_developer(request,id):
    developers=User.objects.get(id=id)
    developers.delete()
    return redirect('/alldevelopers/')       




