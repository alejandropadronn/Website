from django.http import HttpResponse
from django.shortcuts import render

from .models import Article

def article_list(request):
    articles = Article.objects.all()
    output = ' , '.join([str(article) for article in articles])
    return HttpResponse(output)
