from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  photo = models.ImageField(upload_to='profile')
  bio = models.TextField()
  posts_counter = models.PositiveIntegerField('posts counter', default=0)