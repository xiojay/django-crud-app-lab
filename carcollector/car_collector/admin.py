from django.contrib import admin
from .models import Car, Modification, Tag 

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('year', 'make', 'model') 
    search_fields = ('make', 'model')  

@admin.register(Modification)
class ModificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'car')  
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)