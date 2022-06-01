from django.db import models
from django.forms import CharField

# Create your models here.
class Cat(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    height = models.CharField(max_length=45)
    weight = models.CharField(max_length=45)
    lifespan = models.CharField(max_length=15)
    intelligence = models.CharField(max_length=15)
    activity = models.CharField(max_length=15)
    coat = models.CharField(max_length=15)
    vocalness = models.CharField(max_length=20)
    info = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        
