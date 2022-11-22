from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import User
from django.db.models import Count

# Create your views here.
@login_required 
def admindashboard(request):
    role= str(request.user.role)
    print(str(request.user.role.id))
    developers=User.objects.filter(role=3).count()
    managers=User.objects.filter(role=2).count()
    print(developers)
    print(managers)

    all_users = User.objects.all()


    return render (request, 'dashboard/admin/adminhome.html',locals())

# List of all Developers
def alldevelopers(request):
    role= str(request.user.role)

    alldevelopers=User.objects.filter(role=3)
    print(alldevelopers)
    return render (request, 'dashboard/admin/alldevelopers.html',{'alldevelopers':alldevelopers,'role':role})

# List of all Managers
def allmanagers(request):
    role= str(request.user.role)

    allmanagers=User.objects.filter(role=2)
    print(allmanagers)
    return render (request, 'dashboard/admin/allmanagers.html',{'allmanagers':allmanagers,'role':role})

# Update Developer
def update_developers(request,id):
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
        return render(request,'dashboard/admin/update_developer.html',{'developers':developers,'role':role})

# Delete Developer
def delete_developers(request,id):
    developers=User.objects.get(id=id)
    developers.delete()

    return redirect('/alldevelopers/')     

# Update Manager
def update_manager(request,id):
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
                return redirect('/allmanagers/')
        managers=User.objects.get(id=id)
        return render(request,'dashboard/admin/update_manager.html',{'managers':managers,'role':role})

# Delete Manager
def delete_manager(request,id):
    developers=User.objects.get(id=id)
    developers.delete()
    return redirect('/allmanagers/')          
