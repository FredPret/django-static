from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.TextField()
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)