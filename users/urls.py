from django.urls import path 
from .views import login_api , get_user_data , register_api
from knox.views import LogoutView , LogoutAllView

urlpatterns = [
    path("login/" , login_api ) ,
    path("user/" , get_user_data ) ,
    path("register/" , register_api)  , 
    path("logout/" , LogoutView.as_view()) , 
    path("logoutall/" , LogoutAllView.as_view())
    
]
