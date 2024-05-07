from django.contrib import admin
from .models import Article, Settings


# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published')
    search_fields = ('title', 'content')



@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('dest_dir',)
