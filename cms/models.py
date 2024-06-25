from django.core.exceptions import ValidationError
from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = QuillField()
    teaser = models.CharField(blank=True,null=True, max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cms:article_detail", kwargs={"slug": self.slug})
 


class Settings(models.Model):
    dest_dir = models.CharField(max_length=255, help_text="Default directory for exported articles.")
    site_name = models.CharField(max_length=255, default="", help_text="Site name")
    site_headline = models.CharField(max_length=255, default="", help_text="Site headline")
    site_teaser = models.CharField(max_length=255, default="", help_text="Site teaser")

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'
    
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
