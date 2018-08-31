from django.contrib import admin

from .models import Persona, Programa,Asesor,Proyecto, Estudiante


admin.site.register(Persona)
admin.site.register(Programa)
admin.site.register(Asesor)
admin.site.register(Proyecto)
admin.site.register(Estudiante)
