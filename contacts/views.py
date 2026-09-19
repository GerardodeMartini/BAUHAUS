from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .forms import LicitacionContactoForm

def registrar_licitacion(request):
    if request.method == "POST":
        form = LicitacionContactoForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar en la base de datos
            licitacion = form.save()

            # Preparar correo
            asunto = f"Nueva Solicitud de Cotización / Licitación - {licitacion.nombre_empresa}"
            
            # Contexto para el template de correo
            context = {
                "licitacion": licitacion,
                "get_tipo_cliente_display": licitacion.get_tipo_cliente_display()
            }
            
            # Generar contenido HTML y texto plano
            html_body = render_to_string("emails/licitacion_email.html", context)
            text_body = f"""
            Nueva solicitud de cotización/licitación recibida:
            
            Empresa: {licitacion.nombre_empresa}
            CUIT: {licitacion.cuit}
            Email: {licitacion.email}
            Teléfono: {licitacion.telefono}
            Tipo de Cliente: {licitacion.get_tipo_cliente_display()}
            Mensaje: {licitacion.mensaje}
            
            Revisa el panel de administración para más detalles.
            """

            # Crear el correo
            email = EmailMessage(
                subject=asunto,
                body=html_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.EMAIL_RECEIVER],
                reply_to=[licitacion.email]
            )
            email.content_subtype = "html"  # Definir que es HTML

            # Adjuntar archivo si existe
            if licitacion.archivo_adjunto:
                email.attach(
                    licitacion.archivo_adjunto.name,
                    licitacion.archivo_adjunto.read(),
                    licitacion.archivo_adjunto.field.generate_filename(licitacion, licitacion.archivo_adjunto.name)
                )

            # Enviar correo
            try:
                email.send(fail_silently=False)
                messages.success(
                    request, 
                    "Tu solicitud ha sido registrada y enviada con éxito. Un asesor técnico se comunicará a la brevedad."
                )
            except Exception as e:
                # Si falla el envío (ej: mala config de API Key), igual guardamos y mostramos advertencia
                messages.warning(
                    request,
                    "Tu solicitud fue registrada en el sistema, pero ocurrió un problema al enviar la notificación. Nos contactaremos pronto."
                )
            
            # Redirigir de vuelta a la página de origen o donde prefiera el usuario
            next_url = request.POST.get("next") or "catalog:industria"
            return redirect(next_url)
    else:
        form = LicitacionContactoForm()
    
    # En caso de GET, redirige a la landing de industria que es donde está el formulario
    return redirect("catalog:industria")
