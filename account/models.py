from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email Address", unique=True)
    first_name = models.CharField(
        "First Name", max_length=255, null=True, blank=True)
    last_name = models.CharField(
        "Last Name", max_length=255, null=True, blank=True)
    mobile_no = models.CharField("Mobile Number", max_length=50)
    date_of_birth = models.DateField(
        "Date of Birth", auto_now=False, auto_now_add=False, null=True, blank=True)
    address = models.TextField("Address")
    is_staff = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
