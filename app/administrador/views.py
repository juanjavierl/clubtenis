from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView, View, FormView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *

# Create your views here.
def admin(request):
    return render(request,'admin.html')

""" def registro_admin(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente')
            return redirect("/registro_admin/")
    else:
        form = UserRegisterForm()
    
    contexto = {'form':form}
    return render(request,'registro_admin.html',contexto) """

class Registro_admin(CreateView):
    def get(self, request, *args, **kwargs):
        user_form = AdminForm()
        user_perfil_admin = perfil_admin_form()
        return render(request, 'registro_admin.html', {'form': user_form, 'user_perfil':user_perfil_admin})
    def post(self, request, *args, **kwargs):
        user_form = AdminForm(request.POST)
        user_perfil_admin = perfil_admin_form(request.POST)
        if user_form.is_valid() and user_perfil_admin.is_valid():
            user_dato = user_form.save()#guardo los datos del form..
            perfil = PerfilAdminstrador()
            perfil.usuario = user_dato
            perfil.celular = request.POST['celular']
            perfil.ci = request.POST['ci']
            perfil.save()
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            if user is not None:
                login(request, user)
                print ("user",user)
                return redirect("/")
            return redirect("/")
        else:
            return render(request, 'registro_admin.html', {'form': user_form, 'user_perfil':user_perfil_admin})
