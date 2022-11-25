# feedback/tasks.py
import http
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from inhouse_console import settings
from time import sleep

@shared_task(bind=True)
def send_mail_func(self,user_email):
    #operations
    mail_subject= "Thoughtwinit"
    message= '<a href="http://127.0.0.1:8000/account/forgot_password/">click me to visit</a>'
    send_mail(
        subject= mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=True,
    )
    return "Done"
    



