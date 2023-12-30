from typing import Any
from django import forms

from books.models import (Book, Review, Category)

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'


class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = "__all__"