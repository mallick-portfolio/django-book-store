from django.db import models
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.




class Category(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
  name = models.CharField(_("book category"),unique=True, max_length=50)
  slug = models.SlugField(null=True, blank=True)

  def __str__(self) -> str:
    return self.name

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Category, self).save(*args, **kwargs)


class Book(models.Model):
  title = models.CharField(_("book title"), max_length=50)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
  image = models.ImageField(_("book image"), upload_to='books/')
  description = models.TextField(_("book description"))
  price = models.IntegerField(_("book price"))
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='books', null=True, blank=True)

  def __str__(self) -> str:
    return self.title





class Review(models.Model):
  description = models.CharField(_("review description"), max_length=255)
  user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='reviews')
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
  create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


  def __str__(self) -> str:
    return f"{self.user.first_name} {self.user.last_name}"