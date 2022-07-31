from django.urls import path
from .views import *



urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('setname', SetName.as_view(), name="setname"),
    path('profile', ProfileView.as_view(), name="profile"),
    path('updatesocial', updateSocial, name="updatesocial"),
    path('add_skill', addSkills, name="add_skill"),
]
