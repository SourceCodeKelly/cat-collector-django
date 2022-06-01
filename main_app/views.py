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
        name = self.request.GET.get('name')
        
        if name != None:
            context['cats'] = Cat.objects.filter(name__icontains=name)
            context['header'] = f'Searching for {name}'
        else:
            context['cats'] = Cat.objects.all()
            context['header'] = "Popular Cat Breeds"
        return context 
        
        
