from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from .forms import CustomUserCreationForm
# Create your views here.
class indexView(generic.ListView):
  model = User
  template_name = 'users/index.html'
  context_object_name = "users"

  def get_queryset(self):
    return User.objects.all().order_by('-updated_at')

  # return render(request, 'users/index.html')

def register(request):
  # print(dir(request))
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    print(form.is_valid())  
    # if form.is_valid():
    #   user = form.save()
    #   messages.success(request, 'Account Created successfully')
    #   return HttpResponseRedirect(reverse("users:show", args=(user.id)))
  else:
    form = UserCreationForm()

  context = {
    'form':form
  }
  return render(request, 'users/register.html', context)

def show(request, user_id):
  user = get_object_or_404(User, pk=user_id)
  return render(request, 'users/show.html', { 'user':user})