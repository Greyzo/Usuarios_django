from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin


from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()    
    is_staff = models.BooleanField(default=False)
    nombre = models.CharField(max_length=255)
    Pais = models.CharField(max_length=255)
    Ciudad = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    codigoPostal = models.IntegerField()
    NumeroTelefonico = models.CharField(max_length=255)
    identificacion = models.IntegerField(unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_name(self):
        return self.username
