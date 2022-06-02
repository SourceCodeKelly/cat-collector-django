from django.contrib import admin
from .models import Cat, OtherTraits

# Register your models here.
admin.site.register(Cat)
admin.site.register(OtherTraits)