
from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    # path('register/',views.user_register, name='register'),
    # path('login/',views.UserLoginForm.as_view(), name='login'),
    path('register/',views.UserRegistrationForm.as_view(), name='register'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.user_logout, name='logout'),
]
