from django.contrib import admin
from .models import ProyectoObra

@admin.register(ProyectoObra)
class ProyectoObraAdmin(admin.ModelAdmin):
    list_display = ("titulo", "cliente_ubicacion", "categoria_trabajo", "publicado", "orden")
    list_filter = ("publicado", "categoria_trabajo")
    search_fields = ("titulo", "cliente_ubicacion", "descripcion_corta")
    ordering = ("orden", "-id")
