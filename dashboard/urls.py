from django.urls import path, include
from .views import index
from account.rating.views import add_rating,update_rating,delete_rating

urlpatterns = [
    
    path('', index, name='index'),

]
