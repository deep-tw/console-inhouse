from django.shortcuts import render
from django.utils import timezone
import logging

# Create your views here.
logger = logging.getLogger(__name__)
def index(request):
    logger.error("Test!!")
    t = timezone.now()
    logging.debug("hello", t)
    
    return render (request, 'dashboard/index.html')
