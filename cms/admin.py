from django.contrib import admin
from .models import Article, Settings
from django.core.management import call_command
from django.contrib import messages


# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('dest_dir',)

    actions = ['publish_site']
    def publish_site(self, request, queryset):
        call_command('generate_static_site')
        self.message_user(request, "Static site generation initiated.", level=messages.SUCCESS)

    publish_site.short_description = 'Publish Static Site'
