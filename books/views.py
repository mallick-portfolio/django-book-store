from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from books import forms
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormMixin
from django.contrib import messages
from books import models
# Create your views here.




class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

# create category by admin
@method_decorator(login_required, name='dispatch')
class CategoryCreateView(AdminRequiredMixin, SuccessMessageMixin,CreateView):
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
class BookCreateView(AdminRequiredMixin,SuccessMessageMixin, CreateView):
  template_name = "./book/form.html"
  form_class = forms.BookForm
  success_message = 'New book added successfully'
  success_url = reverse_lazy('home')


  def form_valid(self, form):
    obj = form.save(commit=False)
    obj.author = self.request.user
    obj.save()
    return super().form_valid(form)



class BookListView(ListView):
   template_name = './pages/home.html'
   model = models.Book
   context_object_name = 'books'

   def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context.update({
            'categories': models.Category.objects.all(),
        })
        return context

   def get_queryset(self) :
      qs = self.model.objects.all()
      if self.kwargs.get('slug'):
        qs = qs.filter(category__slug=self.kwargs['slug'])
      return qs





class BookDetailView(FormMixin,DetailView):
  context_object_name = 'book'
  model = models.Book
  pk_url_kwarg = 'id'
  template_name = './book/singlebook.html'
  form_class = forms.ReviewForm

  def get_success_url(self):
      return reverse_lazy('book-details', kwargs={'id': self.object.pk})

  def post(self, request, *args, **kwargs):
    print(request.POST)
    if request.method == "POST":
      self.object = self.get_object()
      form = self.get_form()
      if form.is_valid():
          return self.form_valid(form)
      else:
          return self.form_invalid(form)

  def form_valid(self, form):
      obj = form.save(commit=False)
      obj.user = self.request.user
      obj.save()
      return super(BookDetailView, self).form_valid(form)







