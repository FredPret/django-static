import os
import subprocess

from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from django.template.loader import render_to_string
from django.conf import settings

from .models import Article, Settings
from .serializers import ArticleSerializer
from .utils import get_dest_base_dir


# Create your views here.

site_settings = {
    'site_name': Settings.objects.first().site_name
    ,'site_headline': Settings.objects.first().site_headline
    ,'site_teaser': Settings.objects.first().site_teaser
}

def index(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    context = {'articles': articles} | site_settings
    return render(request, 'cms/index.html', context=context)


def about(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    context = {'articles': articles} | site_settings
    return render(request, 'cms/about.html', context=context)


def contact(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    context = {'articles': articles} | site_settings
    return render(request, 'cms/contact.html', context=context)


def article_detail(request, slug):
    print(f'looking for slug {slug}')
    article = Article.objects.get(slug=slug, published=True)
    context = {'article': article} | site_settings
    return render(request, 'cms/post.html', context=context)


def export_to_static(id):
    # deploy command: python manage.py distill-local /private/var/www/nginx_static/django_static/test
    
    # Fetch the article from the database
    article = get_object_or_404(Article, id=id, published=True)
    serializer = ArticleSerializer(article)
    serializer_output_dict = serializer.data
    content = serializer_output_dict.get('content')

    # Use data from serializer
    context = {
        'title': serializer.data['title'],
        'content': content,
        'author': article.author.username,
        'created_at': serializer.data['created_at']
    }

    # Render the template with the article's context
    html_content = render_to_string('cms/static_article_template.html', context=context)

    # Get the directory from Settings or use default
    article_name = article.title.replace(' ', '_').lower()
    dest_dir = os.path.join(get_dest_base_dir(), article_name) # /article/destination/path/article_name/

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # copy html file
    html_file_name = article_name + '.html'
    html_dest_path = os.path.join(dest_dir, html_file_name) # /article/destination/path/article_name/article_name.html

    with open(html_dest_path, 'w') as f:
        f.write(html_content)

    # copy assets folder
    source_assets_path = os.path.join(settings.BASE_DIR, 'cms', 'templates', 'cms', 'assets/')
    destination_assets_path = os.path.join(dest_dir,'assets/')
    try:
        command = [
            'rsync',
            '-av',
            source_assets_path,  # Ensure the source directory ends with a slash
            destination_assets_path
        ]

        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print("rsync output:", result.stdout.decode())
        print("rsync of asset folder done")

    except subprocess.CalledProcessError as e:
        print("rsync failed with the following error:")
        print(e.stderr.decode())
        print(f"when trying to copy from {source_assets_path} to {destination_assets_path}")

    print(f"Article '{article.title}' exported.")
