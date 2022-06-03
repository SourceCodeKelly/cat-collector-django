from django.contrib import admin
from .models import Cat, OtherTraits, List

# Register your models here.
admin.site.register(Cat)
admin.site.register(OtherTraits)
admin.site.register(List)