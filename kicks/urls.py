from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addmember/',views.addmembers),
    path('membersList/', views.members_list),
    
]
