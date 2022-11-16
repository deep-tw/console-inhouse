from django.urls import path, include
from dashboard.admin.views import admindashboard
from dashboard.manager.views import managerdashboard,allprojects
from dashboard.developer.views import developerdashboard

urlpatterns = [

    #----------------Admin --------------------------------
    path('admindashboard/', admindashboard, name='admindashboard'),

    #----------------Manager --------------------------------
    path('managerdashboard/', managerdashboard, name='managerdashboard'),
    path('allprojects/', allprojects, name='allprojects'),


    #----------------Developer --------------------------------
    path('developerdashboard/', developerdashboard, name='developerdashboard'),


]
