from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  photo = models.ImageField(upload_to='profiles', blank=True, null=True, verbose_name='photo')
  bio = models.TextField(blank=True, null=True, verbose_name='Biograthy')
  posts_counter = models.PositiveIntegerField(default=0, null=False, verbose_name='posts counter')