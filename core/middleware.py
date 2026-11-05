import secrets
from django.conf import settings
from django.shortcuts import render, redirect

class ModoProximamenteMiddleware:
    """
    Middleware que controla el acceso según el modo Próximamente:
    - En Producción: si no está autorizado, muestra Próximamente en todas las rutas.
      Permite desbloquear el sitio completo mediante:
        1. Formulario de acceso en /acceso/ con contraseña.
        2. Parámetro directo en la URL: ?clave=Bauhaus@2026
    - Una vez autorizada la sesión, se navega normalmente por todo el sitio.
    - Utiliza secrets.compare_digest para prevenir ataques de temporización (timing attacks).
    - Agrega cabeceras X-Robots-Tag para evitar indexación en buscadores durante la fase de prueba.
    - Nunca intercepta /static/, /media/, /admin/, /acceso/ ni /salir/.
    - En local (127.0.0.1 / localhost): permite navegar siempre.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MODO_PROXIMAMENTE', False):
            # Nunca bloquear archivos estáticos, media, admin ni rutas de autenticación previa
            if (request.path.startswith('/static/') or 
                request.path.startswith('/media/') or 
                request.path.startswith('/admin/') or
                request.path.startswith('/acceso/') or
                request.path.startswith('/salir/')):
                response = self.get_response(request)
                response['X-Robots-Tag'] = 'noindex, nofollow'
                return response

            clave_configurada = getattr(settings, 'CLAVE_ACCESO_PREVIA', 'Bauhaus@2026')

            # Desbloqueo rápido mediante parámetro en URL (ej: https://bauhaus.ar/?clave=Bauhaus@2026)
            clave_url = request.GET.get('clave') or request.GET.get('key')
            if clave_url and secrets.compare_digest(clave_url.strip(), clave_configurada):
                request.session['preview_autorizado'] = True
                request.session['intentos_fallidos'] = 0
                clean_path = request.path
                return redirect(clean_path)

            # Si la sesión ya fue autorizada con la clave, permitir acceso completo
            if request.session.get('preview_autorizado', False):
                response = self.get_response(request)
                response['X-Robots-Tag'] = 'noindex, nofollow'
                response['Cache-Control'] = 'private, no-cache, no-store, must-revalidate'
                return response

            host = request.get_host().split(':')[0]
            is_local = host in ['127.0.0.1', 'localhost', '0.0.0.0']

            # Si es el servidor online de producción y no está autorizado:
            if not is_local:
                response = render(request, 'proximamente.html', {'is_local': False})
                response['X-Robots-Tag'] = 'noindex, nofollow'
                return response

            # En local, sólo si se entra explícitamente a /proximamente/
            if request.path == '/proximamente/':
                response = render(request, 'proximamente.html', {'is_local': True})
                response['X-Robots-Tag'] = 'noindex, nofollow'
                return response

            return self.get_response(request)

        return self.get_response(request)
