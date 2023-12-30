
from django.urls import path
from books import views
urlpatterns = [
    path('create-category/', views.CategoryCreateView.as_view(), name="create-category"),
    path('category/<slug:slug>/', views.BookListView.as_view(), name="category-book"),
    path('add-book/', views.BookCreateView.as_view(), name="add-book"),
    path('<int:id>/', views.BookDetailView.as_view(), name="book-details"),
    path('update/<int:id>/', views.BookUpdateView.as_view(), name="book-update"),
]
