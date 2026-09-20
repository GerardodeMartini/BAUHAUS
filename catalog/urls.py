from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),
    path("proximamente/", views.proximamente, name="proximamente"),
    path("inicio/", views.home_preview, name="home_preview"),
    path("aplicadores/", views.aplicadores, name="aplicadores"),
    path("industria/", views.industria, name="industria"),
]
