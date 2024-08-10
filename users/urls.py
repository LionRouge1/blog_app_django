from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
  path('', views.index_view, name='index'),
  path('register', views.register, name='register')
]
