from django import template
from publications.models import Article

register = template.Library()


@register.simple_tag()
def show_articles():
    return Article.objects.all()