from django.shortcuts import render
from django.contrib import   messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CustomUserCreationForm
# Create your views here.
def index_view(request):
  return render(request, 'users/index.html')

def register(request):
  # print(dir(request))
  if request.method == 'POST':
    form = CustomUserCreationForm()
    if form.is_valid():
      form.save()
      messages.success(request, 'Account Created successfully')
      return HttpResponse()
    else:
      messages.error(request, 'Error in creating user')
  else:
    # messages.error(request, 'Error in creating user')
    # print(messages)
    form = CustomUserCreationForm()
    context = {
      'form':form
    }
  
  return render(request, 'users/register.html', context)