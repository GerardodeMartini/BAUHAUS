from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),
    path("aplicadores/", views.aplicadores, name="aplicadores"),
    path("industria/", views.industria, name="industria"),
]
