from django.contrib import admin

# Register your models here.


from .models import templateModel
from .models import pet

admin.site.register(templateModel)

class petBonitinho(admin.ModelAdmin):
    ordering = ['nome']
    list_display = ['nome', 'tipo', 'nascimento']
    list_filter = ['tipo']
    search_fields = ['nome']
admin.site.register(pet, petBonitinho)