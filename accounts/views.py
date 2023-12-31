from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . import forms
from accounts import models
from books.helpers import send_user_email
from django.contrib.auth.decorators import login_required

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

@login_required
def deposit(request):
  if request.method == "POST":
    a = request.POST['balance']
    amount = int(a)
    account = models.UserBankAccount.objects.filter(user=request.user).first()
    print(account)
    if account is not None:
      if amount > 1000:
        messages.error(request, f'Failded to deposit .Max deposit amount is 1000!!!')
      else:
        account.balance += amount
        account.save()
        messages.success(request, 'Balance added successfully')
        send_user_email(request.user, amount, "Deposite Money", './email/deposit_email.html')
        return redirect('home')
    else:
      messages.error(request, "Something want wrong!!!")
  return render(request, './accounts/addmoney.html')



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


