from django.contrib import admin
from django.db.models import Sum
from .models import Categoria, Producto, EstadisticaVisita

admin.site.site_header = "Bauhaus — Panel de Administración & Marketing"
admin.site.site_title = "Bauhaus Admin"
admin.site.index_title = "Estadísticas de Visitas y Gestión del Sitio"


@admin.register(EstadisticaVisita)
class EstadisticaVisitaAdmin(admin.ModelAdmin):
    list_display = (
        "fecha",
        "pagina",
        "visitas_totales",
        "visitas_movil",
        "visitas_pc",
        "porcentaje_movil",
    )
    list_filter = ("pagina", "fecha")
    date_hierarchy = "fecha"
    ordering = ("-fecha", "pagina")
    readonly_fields = ("fecha", "pagina", "visitas_totales", "visitas_movil", "visitas_pc")

    @admin.display(description="% Celular vs PC")
    def porcentaje_movil(self, obj):
        if not obj.visitas_totales:
            return "0% Celular / 0% PC"
        pct_mov = round((obj.visitas_movil / obj.visitas_totales) * 100)
        pct_pc = 100 - pct_mov
        return f"📱 {pct_mov}% Celular  |  💻 {pct_pc}% PC"


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
