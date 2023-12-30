from typing import Any
from django.shortcuts import render, redirect
from books import forms
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Create your views here.


# create category by admin
@method_decorator(login_required, name='dispatch')
class CategoryCreateView(SuccessMessageMixin,CreateView):
  template_name = "./category/form.html"
  form_class = forms.CategoryForm
  success_url = reverse_lazy('home')
  success_message = 'Category successfully created!'

  def form_valid(self, form):
    obj = form.save(commit=False)
    obj.user = self.request.user
    obj.save()
    return  super().form_valid(form)


# create book by admin
@method_decorator(login_required, name='dispatch')
class BookCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
  template_name = "./book/form.html"
  form_class = forms.BookForm
  success_message = 'New book added successfully'
  success_url = reverse_lazy('home')


  def form_valid(self, form):
    obj = form.save(commit=False)
    obj.author = self.request.user
    obj.save()
    return  super().form_valid(form)



