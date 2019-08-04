from django.urls import path
from . import views


app_name = 'bl'

urlpatterns = [
    path('', views.home , name="home"),
    path('experts', views.experts , name="experts"),
    path('expertDetail/<slug:id>', views.expertDetail , name="expertDetail"),
    path('deleteExpert/<slug:id>', views.deleteExpert , name="deleteExpert"),
    path('addExpert', views.addExpert , name="addExpert"),
    path('logout', views.logout , name="logout"),
    path('editExpert', views.editExpert , name="editExpert"),
    
]