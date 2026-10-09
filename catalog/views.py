from django.conf import settings
from django.shortcuts import render
from .models import Categoria, Producto
from portfolio.models import ProyectoObra
from contacts.forms import LicitacionContactoForm

def proximamente(request):
    return render(request, "proximamente.html")

def home(request):
    return _render_home(request)

def home_preview(request):
    return _render_home(request)

def _render_home(request):
    categorias = Categoria.objects.all()
    productos_destacados = Producto.objects.filter(destacado_home=True, activo=True)[:6]
    proyectos_destacados = ProyectoObra.objects.filter(publicado=True)[:3]
    form = LicitacionContactoForm()
    
    context = {
        "categorias": categorias,
        "productos_destacados": productos_destacados,
        "proyectos_destacados": proyectos_destacados,
        "form": form,
        "active_page": "home",
    }
    return render(request, "home.html", context)

def productos(request):
    productos = Producto.objects.filter(mostrar_en_aplicadores=True, activo=True)
    proyectos = ProyectoObra.objects.filter(publicado=True)[:6]
    form = LicitacionContactoForm()
    
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
    productos = Producto.objects.filter(mostrar_en_industria=True, activo=True)
    proyectos = ProyectoObra.objects.filter(publicado=True)
    form = LicitacionContactoForm()
    
    context = {
        "productos": productos,
        "proyectos": proyectos,
        "form": form,
        "active_page": "industria",
    }
    return render(request, "industria.html", context)
