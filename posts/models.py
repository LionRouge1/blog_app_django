from django.db import models
from users.models import User
from django.contrib.auth import get_user_model

Author = get_user_model()

# Create your models here.
class Post(models.Model):
  author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
  title = models.CharField(blank=False, null=False, max_length=200)
  text = models.TextField(blank=False, null=False)
  comments_counter = models.PositiveIntegerField(default=0, verbose_name='Comments counter')
  likes_counter = models.PositiveIntegerField(default=0, verbose_name='Likes counter')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)