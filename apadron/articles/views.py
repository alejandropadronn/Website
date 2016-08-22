from django.http import HttpResponse
from django.shortcuts import render

from .models import Article

def article_list(request):
    return HttpResponse('Articles Homepage')
