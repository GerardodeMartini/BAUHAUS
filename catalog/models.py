from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    imagen = models.ImageField(upload_to="categorias/", blank=True, null=True, verbose_name="Imagen")
    orden = models.PositiveIntegerField(default=0, verbose_name="Orden de visualización")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["orden", "nombre"]

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Producto(models.Model):
    # Datos Generales (Aplicadores / Comercial)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name="productos", 
        verbose_name="Categoría"
    )
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Producto")
    slug = models.SlugField(max_length=170, unique=True, verbose_name="Slug")
    imagen_principal = models.ImageField(upload_to="productos/", verbose_name="Imagen Principal")
    descripcion_breve = models.TextField(
        max_length=300, 
        verbose_name="Descripción Breve (para Aplicadores)"
    )
    presentacion = models.CharField(
        max_length=100, 
        blank=True, 
        verbose_name="Presentación (ej. Balde 20L, Tambor 200L)"
    )
    orden = models.PositiveIntegerField(default=0, verbose_name="Orden")

    # Datos Técnicos (Industria)
    descripcion_detallada = models.TextField(
        blank=True, 
        verbose_name="Descripción Técnica Detallada"
    )
    rendimiento_m2 = models.CharField(
        max_length=100, 
        blank=True, 
        verbose_name="Rendimiento por m²"
    )
    tiempo_secado = models.CharField(
        max_length=100, 
        blank=True, 
        verbose_name="Tiempo de Secado"
    )
    tipo_superficie = models.CharField(
        max_length=150, 
        blank=True, 
        verbose_name="Preparación de Superficie / Tipo"
    )
    resistencia_quimica = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name="Resistencia Química / Mecánica"
    )
    archivo_pdf = models.FileField(
        upload_to="fichas_tecnicas/", 
        blank=True, 
        null=True, 
        verbose_name="Ficha Técnica (PDF)"
    )

    # Banderas de control
    destacado_home = models.BooleanField(
        default=False, 
        verbose_name="Destacado en Home"
    )
    mostrar_en_aplicadores = models.BooleanField(
        default=True, 
        verbose_name="Mostrar en Aplicadores"
    )
    mostrar_en_industria = models.BooleanField(
        default=True, 
        verbose_name="Mostrar en Industria"
    )
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["orden", "nombre"]

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class EstadisticaVisita(models.Model):
    PAGINA_CHOICES = [
        ("home", "Home (Portada)"),
        ("productos", "Productos"),
        ("industria", "Industria"),
    ]

    fecha = models.DateField(verbose_name="Fecha", db_index=True)
    pagina = models.CharField(
        max_length=30,
        choices=PAGINA_CHOICES,
        verbose_name="Página / Sección",
        db_index=True,
    )
    visitas_totales = models.PositiveIntegerField(default=0, verbose_name="Visitas Totales")
    visitas_movil = models.PositiveIntegerField(default=0, verbose_name="Desde Celular")
    visitas_pc = models.PositiveIntegerField(default=0, verbose_name="Desde PC / Tablet")

    class Meta:
        verbose_name = "Estadística de Visita (Marketing)"
        verbose_name_plural = "Estadísticas de Visitas (Marketing)"
        ordering = ["-fecha", "pagina"]
        unique_together = ("fecha", "pagina")

    def __str__(self):
        return f"{self.fecha} - {self.get_pagina_display()}: {self.visitas_totales} visitas"
