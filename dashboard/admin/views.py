from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required 
def admindashboard(request):
    role= str(request.user.role)

    return render (request, 'dashboard/admin/adminhome.html',locals())


