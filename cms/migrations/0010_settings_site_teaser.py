# Generated by Django 5.0.6 on 2024-06-24 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_settings_site_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='site_teaser',
            field=models.CharField(default='', help_text='Site teaser', max_length=255),
        ),
    ]