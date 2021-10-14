from django import template
from crafts.models import Craft

register = template.Library()


@register.simple_tag()
def show_crafts():
    return Craft.objects.all()