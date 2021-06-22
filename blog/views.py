from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator


# Create your views here.
def home(request, page=1):
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 5)
    articles = paginator.get_page(page)
    context = {
        "articles": articles,
        "category": Category.objects.filter(status=True)
    }
    return render(request, 'blog/home.html', context)


def detail(request, slug):
    context = {
        "article": get_object_or_404(Article.objects.published(), slug=slug)
    }
    return render(request, 'blog/detail.html', context)


def category(request, slug):
    context = {
        "category": get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request, 'blog/category.html', context)
