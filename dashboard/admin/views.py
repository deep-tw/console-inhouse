from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User

# Create your views here.
@login_required 
def admindashboard(request):
    role= str(request.user.role)
    print(str(request.user.role.id))
    developers=User.objects.filter(role=3).count()
    managers=User.objects.filter(role=1).count()

    print(developers)
    print(managers)
    all_users = User.objects.all()

    
    return render (request, 'dashboard/admin/adminhome.html',locals())


