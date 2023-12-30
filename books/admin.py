from django.contrib import admin
from .models import Book, Review, Category
# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
  exclude = ['slug']
  readonly_fields = ['slug']
admin.site.register(Book)
admin.site.register(Review)


admin.site.register(Category, CategoryModelAdmin)

