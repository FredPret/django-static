from django.core.exceptions import ValidationError
from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = QuillField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
 


class Settings(models.Model):
    dest_dir = models.CharField(max_length=255, help_text="Default directory for exported articles.")

    def clean(self):
        # Ensure only one instance exists
        if Settings.objects.exclude(pk=self.pk).exists():
            raise ValidationError("Only one instance of 'Settings' is allowed.")

    def save(self, *args, **kwargs):
        # Run clean method before saving
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Settings (dest_dir={self.dest_dir})"

