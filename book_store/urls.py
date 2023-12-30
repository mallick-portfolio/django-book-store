
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import home
from books.views import BookListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name="home"),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
