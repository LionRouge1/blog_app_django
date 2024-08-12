from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = User

  list_display = ('email', 'name', 'photo', 'bio', 'posts_counter', 'updated_at', 'created_at','is_staff', 'is_active',)
  list_filter = ('email', 'name', 'photo', 'bio', 'posts_counter', 'updated_at', 'created_at', 'is_staff', 'is_active',)
  fieldsets = (
    (None, {'fields': ('email', 'name', 'photo', 'bio', 'posts_counter', 'updated_at', 'created_at','password')}),
    ('Permissions', {'fields': ('is_staff', 'is_active')}),
  )

  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'name', 'photo', 'bio', 'posts_counter', 'updated_at', 'created_at','password1', 'password2', 'is_staff', 'is_active')
    }),
  )

  search_fields = ('email',)
  ordering = ('email',)
  filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)