from django import template
from turnir.models import Turnir

register = template.Library()


@register.simple_tag()
def show_turnirs():
    return Turnir.objects.all()