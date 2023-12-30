
from django.urls import path
from books import views
urlpatterns = [
    path('create-category', views.CategoryCreateView.as_view(), name="create-category"),

]
