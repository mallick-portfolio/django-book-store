from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from .constant import GENDER_TYPE
class CustomUser(AbstractBaseUser, PermissionsMixin):

  first_name = models.CharField(_("first name"), max_length=50, null=True, blank=True)
  last_name = models.CharField(_("last name"), max_length=50, null=True, blank=True)
  email =  models.EmailField(_("email address"), max_length=254, unique= True)
  username =  models.CharField(_("user name"), max_length=254, unique= True, null=True, blank=True)
  birth_date = models.DateField(null=True, blank=True)
  gender = models.CharField(choices=GENDER_TYPE, max_length=20, null=True, blank=True)
  street_address = models.CharField(max_length=100,null=True, blank=True)
  city = models.CharField(max_length= 100,null=True, blank=True)
  postal_code = models.IntegerField(null=True, blank=True)
  country = models.CharField(max_length=100, null=True, blank=True)



  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  date_joined = models.DateTimeField(default=timezone.now)


  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ()

  def __str__(self) -> str:
    return self.email