from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),
    path("proximamente/", views.proximamente, name="proximamente"),
    path("acceso/", views.acceso_preview, name="acceso_preview"),
    path("salir/", views.salir_preview, name="salir_preview"),
    path("inicio/", views.home_preview, name="home_preview"),
    path("aplicadores/", views.aplicadores, name="aplicadores"),
    path("productos/", views.productos, name="productos"),
    path("industria/", views.industria, name="industria"),
]
