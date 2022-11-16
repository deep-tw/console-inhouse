from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required 
def index(request):
    # print(request.user.role, type(request.user.role))
    role= str(request.user.role)
    return render (request, 'dashboard/index.html', locals())
