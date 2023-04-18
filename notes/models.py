from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.

class Note(models.Model) : 
    page_number = models.IntegerField(validators=[MinValueValidator(0)] , null= False , blank=False) 
    pdf = models.CharField(max_length=100 , null= False , blank=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="notes")
    title = models.CharField(max_length=50 , null=True , blank=True )
    note_body = models.CharField(max_length=500)
    


