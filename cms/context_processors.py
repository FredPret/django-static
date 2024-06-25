from .models import Settings

def site_settings(request):
    settings = Settings.objects.first()
    return {
        'site_name': settings.site_name,
        'site_headline': settings.site_headline,
        'site_teaser': settings.site_teaser,
        'about': settings.about,  # Include the new field
    }