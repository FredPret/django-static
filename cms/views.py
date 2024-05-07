from .utils import get_dest_dir
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render
from .models import Article
import os

# Create your views here.


def index(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'cms/index.html', {'articles': articles})


def article_detail(request, id):
    article = Article.objects.get(id=id, published=True)
    return render(request, 'cms/article_detail.html', {'article': article})


def export_to_static(id):
    # Fetch the article from the database
    article = get_object_or_404(Article, id=id, published=True)

    # Render the template with the article's context
    html_content = render_to_string('cms/article_static.html', {'article': article})


    # Get the directory from Settings or use default
    dest_dir = get_dest_dir()

    # Define the full path to store the HTML file
    dest_file = f"{article.title.replace(' ', '_').lower()}.html"
    dest_path = os.path.join(dest_dir, dest_file)

    # Write the content to the file
    with open(dest_path, 'w') as f:
        f.write(html_content)

    print(f"Article '{article.title}' exported to {dest_path}.")
