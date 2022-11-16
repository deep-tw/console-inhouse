from django.urls import path, include
from .views import index
from account.rating.views import add_rating,update_rating,delete_rating,retrieve_rating

urlpatterns = [
    
    path('', index, name='index'),
    path('create_rating/',add_rating,name='create'),
    path('retrieve_rating/',retrieve_rating,name='retrieve'),
    path('update_rating/<int:id>/',update_rating,name='update'),
    path('delete_rating/<int:id>/',delete_rating,name='delete')

]
