from django.urls import path
from .import views
from django.urls import path, include
from dashboard.admin.views import admindashboard,alldevelopers,allmanagers,update_manager,delete_manager,update_developers,delete_developers
from dashboard.manager.views import managerdashboard,allprojects,alldevelopers,update_developer,delete_developer
from dashboard.developer.views import developerdashboard,assignprojects,self_update_developer
from .views import index
from account.rating.views import add_rating,update_rating,delete_rating,retrieve_rating


urlpatterns = [

    #----------------Admin --------------------------------
    path('admindashboard/', admindashboard, name='admindashboard'),
    path('alldevelopers/', alldevelopers, name='alldevelopers'),
    path('update_developers/<int:id>', update_developers, name='update_developers'),
    path('delete_developers/<int:id>', delete_developers, name='delete_developers'),
    path('allmanagers/', allmanagers, name='allmanagers'),
    path('update_manager/<int:id>', update_manager, name='update_manager'),
    path('delete_manager/<int:id>', delete_manager, name='delete_manager'),


    #----------------Manager --------------------------------
    path('managerdashboard/', managerdashboard, name='managerdashboard'),
    path('allprojects/', allprojects, name='allprojects'),
    path('alldevelopers/', alldevelopers, name='alldevelopers'),
    path('update_developer/<int:id>', update_developer, name='update_developer'),
    path('delete_developer/<int:id>', delete_developer, name='delete_developer'),


    #----------------Developer --------------------------------
    path('developerdashboard/', developerdashboard, name='developerdashboard'),
    path('assignprojects/', assignprojects, name='assignprojects'),
    path('self_update_developer/<int:id>', self_update_developer, name='self_update_developer'),


    #-----------------Project --------------------------------------
    path('', views.index, name='index'),
    path('project/',views.project, name='project_create'),
    path('delete/<int:id>/', views.delete_data, name='delete_project'),
    path('update/<int:id>/', views.update_data, name="update_project"),
    # path('log/', views.log, name='log'),
    # path('', index, name='index'),


    #---------------------Ratings------------------------------------
    path('create_rating/',add_rating,name='create'),
    path('retrieve_rating/',retrieve_rating,name='retrieve'),
    path('update_rating/<int:id>/',update_rating,name='update'),
    path('delete_rating/<int:id>/',delete_rating,name='delete')

]