
from django.urls import path
from app.inicio import views
urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('cerrar-sesion', views.cerrarSesion, name='close'),
    path('all-get-users', views.AllGetUsers.as_view(), name='users'),
    path('registerNewUser', views.registerNewUser, name='register'),
    path('show-status-user/<int:pk>',views.UserDetailView.as_view(), name='user'),
    
    path('myperfil', views.MyPerfilUser, name='myperfil'),
    path('change-password/<int:id_user>', views.ChangePassword, name='change-password'),
]
