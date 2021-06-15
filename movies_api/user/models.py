from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_on = models.DateTimeField(auto_now_add=True)
    modifield_on=models.DateTimeField(auto_now=True)

    class Meta:
         db_table='auth_user'




