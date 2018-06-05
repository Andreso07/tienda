from django.urls import path
from usuarios import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.RegistroUsuario.as_view()), name="registrar")
]