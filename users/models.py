from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
  username = None
  name = models.CharField(_('user_name'), blank=False, null=False)
  email = models.EmailField(_('email_address'), unique=True, max_length=200)
  photo = models.ImageField(upload_to='profiles', blank=True, null=True, verbose_name='photo')
  bio = models.TextField(blank=True, null=True, verbose_name='Biograthy')
  posts_counter = models.PositiveIntegerField(default=0, null=False, verbose_name='posts counter')
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  def has_perm(self, perm, obj=None):
    return True
  
  # def is_staff(self):
  #   return self.staff
  
  @property
  def is_admin(self):
    return self.is_superuser
  
  def __str__(self):
    return self.email
  