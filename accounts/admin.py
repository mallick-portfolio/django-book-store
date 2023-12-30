from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = ('email','first_name', 'last_name',  'is_staff', 'is_active')
  list_filter =('email', 'is_staff', 'is_active')

  fieldsets = (
    (None, {
      "fields": ('email', 'username', 'password', 'first_name', 'last_name','birth_date', 'gender', 'street_address', 'city', 'postal_code', 'country'),
    }),
    ("Permissions", {
      "fields" : ("is_staff", "is_active", "groups", "user_permissions"),
    }),
  )

  add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", 'username', 'first_name', 'last_name', "password1", "password2",
                'birth_date', 'gender', 'street_address', 'city', 'postal_code', 'country' , "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
  search_fields = ("email",)
  ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)