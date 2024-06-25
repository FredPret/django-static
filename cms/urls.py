from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_distill import distill_path
from cms.models import Article
from . import views


def get_article_slugs_for_django_distill():
    for article in Article.objects.all():
        yield {'slug': article.slug}


def get_none_for_django_distill():
    return None

        
app_name='cms'
urlpatterns = [
    path('', views.index, name='index'),
    distill_path('', views.index, name='index', distill_func=get_none_for_django_distill, distill_file='index.html'),

    path("articles/<slug:slug>", views.article_detail, name="article_detail"),
    distill_path('articles/<slug:slug>', views.article_detail, name='article_detail', distill_func=get_article_slugs_for_django_distill, distill_file='articles/{slug}.html'),

    path('about/', views.about, name='about'),
    distill_path('about/', views.about, name='about', distill_func=get_none_for_django_distill, distill_file='about.html'),

    path('contact/', views.contact, name='contact'),
    distill_path('contact/', views.contact, name='contact', distill_func=get_none_for_django_distill, distill_file='contact.html'),

]

urlpatterns += staticfiles_urlpatterns()
