from django.urls import path
from .import views
from django.urls import path, include
from .views import index
from account.rating.views import add_rating,update_rating,delete_rating,retrieve_rating

urlpatterns = [
    
    path('', views.index, name='index'),
    path('project/',views.project, name='project_create'),
    path('delete/<int:id>/', views.delete_data, name='delete_project'),
    path('update/<int:id>/', views.update_data, name="update_project"),
    # path('log/', views.log, name='log'),
    # path('', index, name='index'),
    path('create_rating/',add_rating,name='create'),
    path('retrieve_rating/',retrieve_rating,name='retrieve'),
    path('update_rating/<int:id>/',update_rating,name='update'),
    path('delete_rating/<int:id>/',delete_rating,name='delete')

]
