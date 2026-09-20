from django.conf import settings
from django.shortcuts import render

class ModoProximamenteMiddleware:
    """
    Middleware que controla el acceso según el modo Próximamente:
    - En Producción (dominio público): intercepta el 100% de las rutas públicas y muestra Próximamente.
    - En Host Local (127.0.0.1 / localhost): muestra Próximamente en la raíz '/', pero permite navegar
      a /inicio/, /aplicadores/ e /industria/ para que puedas trabajar y ver las modificaciones.
    - No intercepta /static/, /media/ ni /admin/.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MODO_PROXIMAMENTE', False):
            # Nunca bloquear archivos estáticos, media ni el panel de administración
            if (request.path.startswith('/static/') or 
                request.path.startswith('/media/') or 
                request.path.startswith('/admin/')):
                return self.get_response(request)

            host = request.get_host().split(':')[0]
            is_local = host in ['127.0.0.1', 'localhost', '0.0.0.0']

            # Si es el servidor online de producción:
            # Bloqueo total -> Cualquier ruta muestra siempre Próximamente
            if not is_local:
                return render(request, 'proximamente.html', {'is_local': False})

            # Si es el host local de trabajo:
            # En la raíz '/' mostramos Próximamente (con barra de navegación local para cambiar de página)
            if request.path == '/' or request.path == '/proximamente/':
                return render(request, 'proximamente.html', {'is_local': True})

            # En /inicio/, /aplicadores/, /industria/ dejamos pasar para que veas los cambios
            return self.get_response(request)

        return self.get_response(request)
