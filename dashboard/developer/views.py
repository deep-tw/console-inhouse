from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required 
def developerdashboard(request):
    role= str(request.user.role)
    print(str(request.user.role.id))
    return render (request,'dashboard/developer/developerhome.html',locals())
# Create your views here.

