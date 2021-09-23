from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    pass
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)

    user_email = models.CharField(max_length=64)
    superuser = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user_email']