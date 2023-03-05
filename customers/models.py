from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    phone = models.BigIntegerField(max_length=11, unique=True)
    password = models.TextField(max_length=64)
    email = models.EmailField(max_length=200, blank=True)
    address = models.TextField(max_length=300, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=False)
    username = models.CharField(default='',max_length=200,unique=True)
    last_login = models.DateTimeField(auto_now=True, editable=None)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.phone)

