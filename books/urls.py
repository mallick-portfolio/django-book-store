
from django.urls import path
from books import views
urlpatterns = [
    path('create-category/', views.CategoryCreateView.as_view(), name="create-category"),
    path('category/<slug:slug>/', views.BookListView.as_view(), name="category-book"),
    path('add-book/', views.BookCreateView.as_view(), name="add-book"),
    path('<int:id>/', views.BookDetailView.as_view(), name="book-details"),
    path('update/<int:id>/', views.BookUpdateView.as_view(), name="book-update"),
    path('borrow/<int:book_id>/', views.borrow_book, name="borrow-book"),
    path('my-borrowed/', views.my_borrow_book, name="my-borrow-book"),
    path('return-borrowed-book/<int:borrow_id>', views.return_book, name="return-borrowed-book"),
]
