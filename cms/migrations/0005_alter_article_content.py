# Generated by Django 4.1.3 on 2024-05-07 04:38

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0004_article_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=django_quill.fields.QuillField(),
        ),
    ]
