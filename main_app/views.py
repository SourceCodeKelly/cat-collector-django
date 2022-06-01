from django.shortcuts import render
from django.template import Template
from django.views import View #
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Cat

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
#...
class About(TemplateView):
    template_name = 'about.html'
    
        
class CatList(TemplateView):
    template_name = 'cat_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Cat.objects.all()
        return context 
        
        
