from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article
from .views import export_to_static

@receiver(post_save, sender=Article)
def export_article(sender, instance, **kwargs):
    if instance.published:
        export_to_static(instance.id)