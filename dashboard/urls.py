from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('project/',views.project, name='project'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('update/<int:id>/', views.update_data, name="update"),
    path('log/', views.log, name='log')

]
