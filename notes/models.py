from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.

class Note(models.Model) : 
    page = models.IntegerField(validators=[MinValueValidator(0)] , null= False , blank=False) 
    source = models.CharField(max_length=100 , null= False , blank=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="notes")
    title = models.CharField(max_length=50 , null=True , blank=True )
    body = models.CharField(max_length=500)
    image = models.ImageField(null=True , blank=True)
    category = models.CharField(max_length=200)
    color = models.IntegerField(null=True)
    


