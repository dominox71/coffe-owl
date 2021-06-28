from django.contrib import admin
from .models import Pytanie, Wybor

 
class WyboryWLinii(admin.TabularInline):
    model=Wybor
    extra=3
    
class PytanieAdmin(admin.ModelAdmin):
    list_display =('tekst_pytania','data_publikacji','byl_publikowany_ostatnio')
    list_filter=['data_publikacji']
    search_fields =['tekst_pytania']
    fieldsets =[
        (None, {'fields':['tekst_pytania']}),
        ('Informacje o czasie', {'fields':['data_publikacji'], 'classes':['collapse']}),
    ]
    inlines =[WyboryWLinii]        
# Register your models here.
admin.site.register(Pytanie,PytanieAdmin)
admin.site.register(Wybor)

