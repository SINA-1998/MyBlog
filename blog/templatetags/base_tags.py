from django import template
from ..models import Category

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


@register.inclusion_tag("../templates/registration/partials/link.html")
def link(request, link_name, content):
    return {
        "request": request,
        "link_name": link_name,
        "content": content,
        "link": "account:{}".format(link_name),
    }
