from django import template
from menu.models import MenuItem
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name)
    return render_to_string('menu_item.html', {'items': menu_items})
