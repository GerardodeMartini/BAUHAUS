from django.db import models

class LicitacionContacto(models.Model):
    TIPO_CLIENTE_CHOICES = [
        ('aplicador', 'Aplicador / Profesional'),
        ('industria', 'Empresa / Industria'),
    ]

    nombre_empresa = models.CharField(max_length=150, verbose_name="Nombre / Razón Social Empresa")
    cuit = models.CharField(max_length=20, verbose_name="CUIT")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=50, verbose_name="Teléfono de Contacto")
    tipo_cliente = models.CharField(
        max_length=20, 
        choices=TIPO_CLIENTE_CHOICES, 
        default='industria', 
        verbose_name="Tipo de Cliente"
    )
    mensaje = models.TextField(verbose_name="Mensaje o Requerimiento")
    archivo_adjunto = models.FileField(
        upload_to="licitaciones/adjuntos/", 
        blank=True, 
        null=True, 
        verbose_name="Pliego / Archivo Adjunto (Opcional)"
    )
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        verbose_name = "Contacto de Licitación"
        verbose_name_plural = "Contactos de Licitaciones"
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.nombre_empresa} - {self.email} ({self.get_tipo_cliente_display()})"
