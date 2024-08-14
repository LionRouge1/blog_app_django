from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import fields
from django import forms
from .models import User
from django.contrib.auth import get_user_model

Author = get_user_model()
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
  # first_name = forms.CharField(label='First name', min_length=2, max_length=100)
  # last_name = forms.CharField(label='Last name', min_length=2, max_length=100)
  # username = forms.CharField(label='Username', min_length=5, max_length=150)
  # email = forms.EmailField(label='Email')
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('email', 'name', 'bio',)

  # def username_clean(self):  
  #   username = self.cleaned_data['username'].lower()  
  #   new = Author.objects.filter(username = username)  
  #   if new.count():  
  #     raise forms.ValidationError("User Already Exist")  
  #   return username  
  
  def clean_email(self):  
    email = self.cleaned_data.get('email') 
    user = Author.objects.filter(email=email)  
    if user.exists():  
      raise forms.ValidationError("Email Already Exist")  
    return email  
  
  # def clean_password2(self):  
  #   password1 = self.cleaned_data['password1']  
  #   password2 = self.cleaned_data['password2']  
  
  #   if password1 and password2 and password1 != password2:  
  #     raise forms.ValidationError("Password don't match")  
  #   return password2  

  def clean(self):
    cleaned_data = super().clean()
    password1 = cleaned_data.get('password1')
    password2 = cleaned_data.get('password2')

    if password1 is not None and password1 != password2:
      self.add_error('password2', 'Your passwords must match')
    return cleaned_data
  
  def save(self, commit = True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user
  
    # user = Author.objects.create_user(  
    #   # self.cleaned_data['first_name'],
    #   # self.cleaned_data['last_name'],
    #   self.cleaned_data['username'],  
    #   self.cleaned_data['email'],  
    #   self.cleaned_data['password1']  
    # )  
    # return user

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = User
    fields = ('name', 'photo', 'bio',)
  
class LoginForm(forms.Form):
  email = forms.EmailField(label="Enter email")
  password = forms.CharField(label='Enter password', widget=forms.PasswordInput)