from django.db import models
from django.contrib.auth.models import User


class PerfilAdminstrador(models.Model):
    usuario = models.OneToOneField(User, related_name='perfil', on_delete = models.CASCADE)
    celular = models.PositiveIntegerField()
    ci = models.CharField('Nro de CI', max_length=15)

    # TODO: Define fields here

    class Meta:
        """Meta definition for ClientePerfil."""

        verbose_name = 'PerfilAdminstrador'
        verbose_name_plural = 'PerfilAdminstradors'

    def __str__(self):
        """Unicode representation of ClientePerfil."""
        return "%s"%(self.celular)