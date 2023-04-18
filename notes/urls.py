from django.urls import path 
from .views import get_user_notes
urlpatterns = [
    path("" , get_user_notes)
]
