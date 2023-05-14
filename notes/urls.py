from django.urls import path 
from .views import  single_note, get_create_notes , uploadImage
urlpatterns = [
    # path("" , get_user_notes) , 
    path("<int:pk>/" , single_note) , 
    path("" , get_create_notes) , 
    path("uploadimage/<int:pk>/" , uploadImage)
]
