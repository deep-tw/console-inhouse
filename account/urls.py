from django.urls import path, include
from .views import login,registration,logoutview,home


urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('logout/',logoutview,name='logout'),
    path('registration/',registration,name='registration'),
    path('social-auth/', include('social_django.urls', namespace='social')),

]
