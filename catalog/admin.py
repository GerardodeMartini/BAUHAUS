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

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response

        nombres_paginas = dict(EstadisticaVisita.PAGINA_CHOICES)
        por_pagina = []
        for codigo, etiqueta in EstadisticaVisita.PAGINA_CHOICES:
            agg = qs.filter(pagina=codigo).aggregate(
                totales=Sum("visitas_totales"),
                movil=Sum("visitas_movil"),
                pc=Sum("visitas_pc"),
            )
            t = agg["totales"] or 0
            m = agg["movil"] or 0
            p = agg["pc"] or 0
            pct_m = round((m / t) * 100) if t else 0
            pct_p = (100 - pct_m) if t else 0
            por_pagina.append({
                "pagina": etiqueta,
                "visitas_totales": t,
                "visitas_movil": m,
                "visitas_pc": p,
                "porcentaje": f"📱 {pct_m}% Celular  |  💻 {pct_p}% PC" if t else "0% Celular / 0% PC",
            })

        agg_total = qs.aggregate(
            totales=Sum("visitas_totales"),
            movil=Sum("visitas_movil"),
            pc=Sum("visitas_pc"),
        )
        gt = agg_total["totales"] or 0
        gm = agg_total["movil"] or 0
        gp = agg_total["pc"] or 0
        gpct_m = round((gm / gt) * 100) if gt else 0
        gpct_p = (100 - gpct_m) if gt else 0

        response.context_data["resumen_por_pagina"] = por_pagina
        response.context_data["resumen_total_general"] = {
            "visitas_totales": gt,
            "visitas_movil": gm,
            "visitas_pc": gp,
            "porcentaje": f"📱 {gpct_m}% Celular  |  💻 {gpct_p}% PC" if gt else "0% Celular / 0% PC",
        }
        return response


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
