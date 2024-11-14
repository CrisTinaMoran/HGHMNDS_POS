from django.db import models
from django.contrib.auth.models import users

class Item(models.Model):
    Prd_name = models.CharField(max_length=max)
    Description =  models.TextField()
    price = models.IntegerField()
    qty =  models.Intergerfield()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 
    
    