from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.urls import reverse, reverse_lazy
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

class SignUpView(generic.CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
  # print(dir(request))
  # if request.method == 'POST':
  #   form = UserCreationForm(request.POST)
  #   print(form.is_valid())  
  #   # if form.is_valid():
  #   #   user = form.save()
  #   #   messages.success(request, 'Account Created successfully')
  #   #   return HttpResponseRedirect(reverse("users:show", args=(user.id)))
  # else:
  #   form = UserCreationForm()

  # context = {
  #   'form':form
  # }
  # return render(request, 'users/register.html', context)

# def login(request):
#   if request.method == 'POST':
#     pass
#   user = LoginForm()
#   return render(request, 'users/login.html', {'form':user})
# @login_required
def show(request, user_id):
  user = get_object_or_404(User, pk=user_id)
  return render(request, 'users/show.html', { 'user':user})

class EditView(LoginRequiredMixin, generic.edit.UpdateView):
  model = User
  form_class = CustomUserChangeForm
  template_name = 'registration/edit.html'

  def get_object(self):
    return self.request.user
  
  def get_success_url(self):
    return reverse_lazy('users:show', args=[self.request.user.id])
