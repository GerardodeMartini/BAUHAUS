from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "slug", "orden")
    prepopulated_fields = {"slug": ("nombre",)}
    search_fields = ("nombre", "descripcion")
    ordering = ("orden", "nombre")


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre", 
        "categoria", 
        "presentacion", 
        "orden", 
        "destacado_home", 
        "mostrar_en_aplicadores", 
        "mostrar_en_industria", 
        "activo"
    )
    list_filter = (
        "categoria", 
        "destacado_home", 
        "mostrar_en_aplicadores", 
        "mostrar_en_industria", 
        "activo"
    )
    search_fields = ("nombre", "descripcion_breve", "descripcion_detallada")
    prepopulated_fields = {"slug": ("nombre",)}
    ordering = ("orden", "nombre")

    fieldsets = (
        ("Datos Generales (Comercial / Aplicadores)", {
            "fields": (
                "nombre", 
                "slug", 
                "categoria", 
                "imagen_principal", 
                "descripcion_breve", 
                "presentacion", 
                "orden"
            )
        }),
        ("Datos Técnicos (Empresas / Industria)", {
            "fields": (
                "descripcion_detallada", 
                "rendimiento_m2", 
                "tiempo_secado", 
                "tipo_superficie", 
                "resistencia_quimica", 
                "archivo_pdf"
            )
        }),
        ("Banderas de Control", {
            "fields": (
                "destacado_home", 
                "mostrar_en_aplicadores", 
                "mostrar_en_industria", 
                "activo"
            )
        }),
    )
