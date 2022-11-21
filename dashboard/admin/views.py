from django.shortcuts import render
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


def alldevelopers(request):
    role= str(request.user.role)

    alldevelopers=User.objects.filter(role=3)
    print(alldevelopers)
    return render (request, 'dashboard/admin/alldevelopers.html',locals())


def allmanagers(request):
    role= str(request.user.role)

    allmanagers=User.objects.filter(role=2)
    print(allmanagers)
    return render (request, 'dashboard/admin/allmanagers.html',locals())
