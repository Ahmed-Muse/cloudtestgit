from django.urls import path
app_name='login'
from . import views

urlpatterns = [
	path('', views.userLoginPage, name="userLoginPage"),#this is the home page
    path('New/User/Registration/', views.newUserRegistration, name="newUserRegistration"),#this is the home page
    path('logout', views.logoutpage, name="logout"),#this is the home page


    ############################################
    path('Custom/User/Creation', views.CustomUser, name="CustomUser"),#this is the home page
    path('/New/Custom/User/Creation', views.newCustomUserRegistration, name="newCustomUserRegistration"),#this is the home page


    








    path('user-profile', views.systemUserProfile, name="user-profile"),#this is the home page
    path('edit-profile', views.editProfile, name="edit-profile"),

     path('User/Profile/Create/', views.CreateUserProfile, name="CreateUserProfile"),
    path('Change/User/password/create/new/', views.changeUserPassword, name="changeUserPassword"),

    
	
]