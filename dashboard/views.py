from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils import timezone
import logging

# Create your views here.
logger = logging.getLogger(__name__)
@login_required 
def index(request):
    logger.error("Test!!")
    t = timezone.now()
    logging.debug("hello", t)
    
    return render (request, 'dashboard/index.html')
    
