#encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import *


class AdminForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, label="Nombre Completo")
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','email','username','password1', 'password2')
    def clean_first(self):
        if self.cleaned_data['first_name'] == "":
            raise forms.ValidationError('Escriba su nombre')

    def save(self,commit=True):
        user=super(AdminForm,self).save(commit=False)
        user.username=self.cleaned_data.get("email")
        if commit:
            user.is_active = True
            user.is_staff = False
            user.is_superuser = False
            user.save()
        return user

class perfil_admin_form(forms.ModelForm):
    """FORMNAME definition."""
    class Meta:
        model = PerfilAdminstrador
        fields = ['celular','ci']