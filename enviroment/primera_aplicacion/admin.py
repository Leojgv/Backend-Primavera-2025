from django.contrib import admin
from .models import Direccion,Autor,Comuna,Nacionalidad

# Register your models here.

admin.site.register(Direccion)
admin.site.register(Autor)
admin.site.register(Comuna)
admin.site.register(Nacionalidad)