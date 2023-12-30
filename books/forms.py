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
    fields = ['title', 'category', 'image', 'description', 'price']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    for field in self.fields:
        self.fields[field].widget.attrs.update({
            'class' : (
                'appearance-none block w-full bg-gray-200 '
                'text-gray-700 border border-gray-200 rounded '
                'py-3 px-4 leading-tight focus:outline-none '
                'focus:bg-white focus:border-gray-500'
            )
        })