from django.urls import path
from .views import *



urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('setname', SetName.as_view(), name="setname"),
    path('profile', ProfileView.as_view(), name="profile"),
    path('settings', SettingsView.as_view(), name="settings"),
    path('updatesocial', updateSocial, name="updatesocial"),
    path('addbioprofile', addBioNProfile, name="addbioprofile"),
    path('allusers', AllUsers.as_view(), name="allusers"),
    path('addusers', RegisterUser.as_view(), name="addusers"),
]
