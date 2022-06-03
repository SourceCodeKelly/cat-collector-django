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
    info = models.TextField(max_length=1500)
    preview = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        
class OtherTraits(models.Model):
    
    other_trait = models.CharField(max_length=20)
    trait_info = models.TextField(max_length=500)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='other_traits')
    
    def __str(self):
        return self.other_trait
    
class List(models.Model):
    title = models.CharField(max_length=150)
    cats = models.ManyToManyField(Cat)
    
    def __str__(self):
        return self.title