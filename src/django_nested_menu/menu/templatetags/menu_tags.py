from types import SimpleNamespace
from typing import Dict, List, Union

from django import template
from django.db import connection
from django.template.loader import render_to_string
from menu.models import MenuItem
from menu.services import get_hierarchical_menu


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    current_url = request.path[:-1]
    hierarchical_menu_items = get_hierarchical_menu(menu_name, current_url)
    try:
        return render_to_string(
            'menu/menu.html', {'items': hierarchical_menu_items}
        )
    except Exception as e:
        print(f"Exception in draw_menu() for {menu_name=}")
        print(f"Exception type: {type(e)}")
        print(e)
        return ''


# @register.inclusion_tag('menu/menu.html')
# def draw_menu(menu_name):
#     root_items = MenuItem.objects.filter(name=menu_name, parent=None)
#     return {'menu_items': root_items}
