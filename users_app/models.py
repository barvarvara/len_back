from django.core.validators import RegexValidator
from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser


class UserAccounts(AbstractUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=14, unique=True, verbose_name='номер телефона')

    is_active = models.BooleanField(default=True, verbose_name='Статус активности')
    is_staff = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_accounts'

    def __str__(self):
        return self.name + " " + self.email + " " + self.phone
