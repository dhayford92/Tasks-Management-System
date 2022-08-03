from django.urls import path
from .views import *



urlpatterns = [
    path('admindash/', DashboardAdmin.as_view(), name="admindash"),
    path('addproject/', AddProject.as_view(), name="addproject"),
    path('allproject/', allProject, name="allproject"),
    path('finip/<int:id>', allProject, name="finip"),
    path('delete-pro/<int:id>', allProject, name="delete-pro"),
    path('edit-project/<int:id>', ProjectDetail.as_view(), name="edit-project"),
    path('addtask/<int:id>', AddTask.as_view(), name="addtask"),
    path('alltask', ViewTask.as_view(), name="alltask"),
    path('edittask/<int:id>/<int:taskId>', EditTask.as_view(), name="edittask"),
]
