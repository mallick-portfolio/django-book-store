from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . import forms
from accounts import models
# Create your views here.

def user_logout(request):
  logout(request)
  messages.success(request, "Logout successfully!!!")
  return redirect('login')


def login_user(request):
  if request.method == "POST":
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)
    if user is not None:
      print(user)
      login(request, user)
      messages.success(request, "User login successfull!!!")
      return redirect('home')
    else:
      messages.error(request,"Your email or password not correct")
      return render(request, './accounts/login.html')
  else:
    return render(request, './accounts/login.html')



class UserRegistrationForm(FormView):
  form_class = forms.CustomUserCreationForm
  template_name = './accounts/form.html'
  success_url = reverse_lazy('home')

  def form_valid(self,form):

    user = form.save()
    messages.success(self.request, "Your register successfully!!!")
    models.UserBankAccount.objects.create(user=user, account_no=10000 + user.id, balance=0)
    login(self.request, user)
    return super().form_valid(form)
