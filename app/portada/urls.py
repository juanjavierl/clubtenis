

from django.urls import include, path
from . import views
from app.administrador import views

urlpatterns = [
    path('registro_admin', views.Registro_admin.as_view(), name='registro_admin'),
    
]