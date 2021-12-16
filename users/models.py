from django.db import models
from django.contrib.auth.models import AbstractUser

from birthday import BirthdayField, BirthdayManager


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    birthday = BirthdayField(null=True)

