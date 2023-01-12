from django.urls import path, include
from .views import loginview
from . import views
from account import views

urlpatterns = [
    path('',loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('registration/',   views.registration,name='registration'),
    path('change_password/',views.change_password,name='change_password'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('new_password/',views.send_mail_to_all,name='new_password'),
    path('forgot_password/',views.reset_password,name='forgot_password'),
]
