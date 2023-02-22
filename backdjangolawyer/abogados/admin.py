from django.contrib import admin
from .models import Category,Abogado


class CategoriaAdmin(admin.ModelAdmin):

    readonly_fields= ('created','updated')

class AbogadoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') 

admin.site.register(Category,CategoriaAdmin)
admin.site.register(Abogado,AbogadoAdmin)       
# Register your models here.
