from django.db import models

class ProyectoObra(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título del Proyecto")
    cliente_ubicacion = models.CharField(max_length=200, verbose_name="Cliente / Ubicación")
    categoria_trabajo = models.CharField(
        max_length=100, 
        verbose_name="Categoría de Trabajo (ej. Epoxi en pisos, Impermeabilización)"
    )
    imagen_antes = models.ImageField(
        upload_to="portfolio/antes/", 
        blank=True, 
        null=True, 
        verbose_name="Imagen Antes (Opcional)"
    )
    imagen_despues = models.ImageField(
        upload_to="portfolio/despues/", 
        verbose_name="Imagen Después / Resultado"
    )
    descripcion_corta = models.TextField(
        max_length=400, 
        verbose_name="Descripción Corta del Caso"
    )
    publicado = models.BooleanField(default=True, verbose_name="Publicado")
    orden = models.PositiveIntegerField(default=0, verbose_name="Orden de visualización")

    class Meta:
        verbose_name = "Proyecto / Obra"
        verbose_name_plural = "Proyectos y Obras"
        ordering = ["orden", "-id"]

    def __str__(self):
        return f"{self.titulo} - {self.cliente_ubicacion}"
