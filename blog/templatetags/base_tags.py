from django import template
from django.db.models import Count, Q
from datetime import datetime, timedelta
from ..models import Category, Article

register = template.Library()


@register.simple_tag
def site_title():
    return 'وبــــلاگـ مــن | My Blog'


@register.simple_tag
def nav_title():
    return 'وبــــلاگـ مــن'


@register.inclusion_tag("../templates/blog/partials/category_navbar.html")
def category_navbar():
    return {
        "category": Category.objects.filter(status=True)
    }


@register.inclusion_tag("../templates/blog/partials/popular_articles.html")
def popular_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        "popular_articles": Article.objects.published().annotate(
            count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count',
                                                                                        '-publish')[:5]
    }


@register.inclusion_tag("../templates/registration/partials/link.html")
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "content": content,
        "classes": classes,
        "link": "account:{}".format(link_name),
    }
