from django.urls import include, path
from . import views

urlpatterns = [
    path('xyz/', views.admin, name='admin'),
    path('registro_admin/', views.Registro_admin.as_view(), name='registro_admin'),
    
]