from django.urls import path
from . import views

app_name='cms'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
]