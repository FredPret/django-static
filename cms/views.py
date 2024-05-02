from django.shortcuts import render
from django.template import Template

from .models import Article


# Create your views here.


def index(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'cms/index.html', {'articles': articles})


def article_detail(request, id):
    article = Article.objects.get(id=id, published=True)
    return render(request, 'cms/article_detail.html', {'article': article})




from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from .models import Article
import os

def export_to_static(id):
    # Fetch the article from the database
    article = get_object_or_404(Article, id=id, published=True)

    # Render the template with the article's context
    html_content = render_to_string('cms/article_static.html', {'article': article})

    # Define the destination path
    dest_dir = '/private/var/www/nginx_static/django_static' #'/var/www/nginx'
    dest_file = f"{article.title.replace(' ', '_').lower()}.html"
    dest_path = os.path.join(dest_dir, dest_file)

    # Write the content to the static file
    with open(dest_path, 'w') as f:
        f.write(html_content)

    print(f"Article '{article.title}' exported to {dest_path}.")