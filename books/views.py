from django.shortcuts import render
from books import forms
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
  template_name = "./category/form.html"
  form_class = forms.CategoryForm
  success_url = reverse_lazy('home')


  def form_valid(self, form):
    obj = form.save(commit=False)
    obj.user = self.request.user
    obj.save()
    return  super().form_valid(form)

