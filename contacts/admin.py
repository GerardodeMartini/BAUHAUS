from django.contrib import admin
from .models import LicitacionContacto

@admin.register(LicitacionContacto)
class LicitacionContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre_empresa", "cuit", "email", "telefono", "tipo_cliente", "fecha")
    list_filter = ("tipo_cliente", "fecha")
    search_fields = ("nombre_empresa", "cuit", "email", "mensaje")
    readonly_fields = ("fecha",)
    ordering = ("-fecha",)
