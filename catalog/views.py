import secrets
import time
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Categoria, Producto
from portfolio.models import ProyectoObra
from contacts.forms import LicitacionContactoForm

def proximamente(request):
    return render(request, "proximamente.html")

def acceso_preview(request):
    error = None
    clave_configurada = getattr(settings, 'CLAVE_ACCESO_PREVIA', 'Bauhaus@2026')
    
    # Si ya está autorizado por sesión o cookie, redirigir directo a Home
    ya_autorizado = False
    try:
        if request.session.get('preview_autorizado', False):
            ya_autorizado = True
    except Exception:
        pass
    if not ya_autorizado:
        try:
            if request.get_signed_cookie('preview_autorizado', default=None) == '1':
                ya_autorizado = True
        except Exception:
            pass

    if ya_autorizado:
        return redirect('catalog:home')
        
    # Protección contra ataques de fuerza bruta (máximo 5 intentos en 15 minutos)
    ahora = int(time.time())
    intentos = 0
    ultimo_intento = ahora
    try:
        intentos = request.session.get('intentos_fallidos', 0)
        ultimo_intento = request.session.get('ultimo_intento_tiempo', ahora)
    except Exception:
        pass
    
    # Si pasaron más de 15 minutos (900 seg), reiniciar contador
    if ahora - ultimo_intento > 900:
        intentos = 0
        try:
            request.session['intentos_fallidos'] = 0
        except Exception:
            pass

    if intentos >= 5:
        minutos_restantes = max(1, (900 - (ahora - ultimo_intento)) // 60)
        error = f'Demasiados intentos fallidos. Por seguridad, el acceso está bloqueado temporalmente por {minutos_restantes} minuto(s).'
        return render(request, 'acceso_preview.html', {'error': error, 'bloqueado': True})
        
    if request.method == 'POST':
        clave_ingresada = request.POST.get('clave', '').strip()
        if secrets.compare_digest(clave_ingresada, clave_configurada):
            try:
                request.session['preview_autorizado'] = True
                request.session['intentos_fallidos'] = 0
            except Exception:
                pass
            resp = redirect('catalog:home')
            resp.set_signed_cookie('preview_autorizado', '1', max_age=86400*30, httponly=True, samesite='Lax')
            return resp
        else:
            intentos += 1
            try:
                request.session['intentos_fallidos'] = intentos
                request.session['ultimo_intento_tiempo'] = ahora
            except Exception:
                pass
            restantes = 5 - intentos
            if restantes > 0:
                error = f'La contraseña ingresada no es correcta. Te quedan {restantes} intento(s).'
            else:
                error = 'Demasiados intentos fallidos. El acceso ha sido bloqueado temporalmente por 15 minutos.'
            
    clave_get = request.GET.get('clave') or request.GET.get('key')
    if clave_get and secrets.compare_digest(clave_get.strip(), clave_configurada):
        try:
            request.session['preview_autorizado'] = True
            request.session['intentos_fallidos'] = 0
        except Exception:
            pass
        resp = redirect('catalog:home')
        resp.set_signed_cookie('preview_autorizado', '1', max_age=86400*30, httponly=True, samesite='Lax')
        return resp
        
    return render(request, 'acceso_preview.html', {'error': error})

def salir_preview(request):
    try:
        request.session.pop('preview_autorizado', None)
    except Exception:
        pass
    resp = redirect('catalog:home')
    resp.delete_cookie('preview_autorizado')
    return resp

def home(request):
    return _render_home(request)

def home_preview(request):
    return _render_home(request)

def _render_home(request):
    try:
        categorias = list(Categoria.objects.all())
        productos_destacados = list(Producto.objects.filter(destacado_home=True, activo=True)[:6])
        proyectos_destacados = list(ProyectoObra.objects.filter(publicado=True)[:3])
    except Exception:
        categorias = []
        productos_destacados = []
        proyectos_destacados = []
        
    try:
        form = LicitacionContactoForm()
    except Exception:
        form = None
    
    context = {
        "categorias": categorias,
        "productos_destacados": productos_destacados,
        "proyectos_destacados": proyectos_destacados,
        "form": form,
        "active_page": "home",
    }
    return render(request, "home.html", context)

def productos(request):
    try:
        productos = list(Producto.objects.filter(mostrar_en_aplicadores=True, activo=True))
        proyectos = list(ProyectoObra.objects.filter(publicado=True)[:6])
    except Exception:
        productos = []
        proyectos = []
        
    try:
        form = LicitacionContactoForm()
    except Exception:
        form = None
    
    context = {
        "productos": productos,
        "proyectos": proyectos,
        "form": form,
        "active_page": "productos",
    }
    return render(request, "productos.html", context)

# Alias para retrocompatibilidad
aplicadores = productos

def industria(request):
    try:
        productos = list(Producto.objects.filter(mostrar_en_industria=True, activo=True))
        proyectos = list(ProyectoObra.objects.filter(publicado=True))
    except Exception:
        productos = []
        proyectos = []
        
    try:
        form = LicitacionContactoForm()
    except Exception:
        form = None
    
    context = {
        "productos": productos,
        "proyectos": proyectos,
        "form": form,
        "active_page": "industria",
    }
    return render(request, "industria.html", context)
