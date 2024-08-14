from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
  path('', views.indexView.as_view(), name='index'),
  path('signup/', views.SignUpView.as_view(), name='signup'),
  path('edit/', views.EditView.as_view(), name='edit'),
  # path('login', views.login, name='login'),
  path('<int:user_id>/', views.show, name='show'),
]
