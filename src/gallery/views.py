from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


def index(request):
    latest_article_list = Article.objects.order_by("-pub_date")[:10]
    context = {"latest_article_list": latest_article_list}
    return render(request, "gallery/index.html", context)

def detail(request, article_id):
    article_data = Article.objects.get(pk=article_id)
    context = {"article_data": article_data}
    return render(request, "gallery/detail.html", context)