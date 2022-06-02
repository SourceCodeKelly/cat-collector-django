from django.shortcuts import render
from django.template import Template
from django.views import View #
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

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
        
class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'img', 'height', 'weight', 'lifespan', 'intelligence', 'activity', 'coat', 'vocalness', 'info']
    template_name = 'cat_create.html'
    
    def get_success_url(self):
        return reverse('cat_details', kwargs={'pk': self.object.pk})
    
class CatDetails(DetailView):
    model = Cat
    template_name = 'cat_details.html'
    
class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'img', 'height', 'weight', 'lifespan', 'intelligence', 'activity', 'coat', 'vocalness', 'info']
    template_name = 'cat_update.html'
    
    def get_success_url(self):
        return reverse('cat_details', kwargs={'pk': self.object.pk})
    
class CatDelete(DeleteView):
    model = Cat
    template_name = 'cat_delete.html'
    success_url = '/cats/'