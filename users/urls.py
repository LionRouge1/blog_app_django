from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
  path('', views.indexView.as_view(), name='index'),
  path('register', views.register, name='register'),
  path('<int:user_id>/', views.show, name='show'),
]
