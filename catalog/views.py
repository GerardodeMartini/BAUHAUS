from django.shortcuts import render
from .models import Categoria, Producto
from portfolio.models import ProyectoObra
from contacts.forms import LicitacionContactoForm

def home(request):
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

def aplicadores(request):
    productos = Producto.objects.filter(mostrar_en_aplicadores=True, activo=True)
    # Filtrar obras comerciales/cotidianas (puedes clasificar por palabra clave o mostrar todas)
    proyectos = ProyectoObra.objects.filter(publicado=True)[:6]
    form = LicitacionContactoForm()
    
    context = {
        "productos": productos,
        "proyectos": proyectos,
        "form": form,
        "active_page": "aplicadores",
    }
    return render(request, "aplicadores.html", context)

def industria(request):
    productos = Producto.objects.filter(mostrar_en_industria=True, activo=True)
    # Filtrar obras de escala industrial
    proyectos = ProyectoObra.objects.filter(publicado=True)
    
    # Formulario para licitaciones
    form = LicitacionContactoForm()
    
    context = {
        "productos": productos,
        "proyectos": proyectos,
        "form": form,
        "active_page": "industria",
    }
    return render(request, "industria.html", context)
