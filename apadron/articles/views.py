from django.http import HttpResponse
from django.shortcuts import render

from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles':articles})
