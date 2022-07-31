from django.urls import path
from .views import *



urlpatterns = [
    path('admindash/', DashboardAdmin.as_view(), name="admindash"),
    path('addproject/', AddProject.as_view(), name="addproject"),
    path('allproject/', allProject, name="allproject"),
    path('addtask/', AddTask.as_view(), name="addtask"),
]
