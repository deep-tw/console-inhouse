from django.urls import path, include
from .views import loginview,registration,logoutview,home,change_password
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),
    path('registration/',registration,name='registration'),
    path('change_password/',change_password,name='change_password'),
    path('social-auth/', include('social_django.urls', namespace='social')),
   
]

