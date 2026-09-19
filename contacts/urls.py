from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("registrar-licitacion/", views.registrar_licitacion, name="registrar_licitacion"),
]
