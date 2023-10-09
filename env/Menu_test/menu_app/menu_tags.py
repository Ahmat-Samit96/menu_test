from django import template
from .models import MenuItem


register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name).first()

    if menu_items:
        return render_menu(menu_items)

def render_menu(menu_item):
    menu_html = '<ul>'
    for item in menu_item.children.all():
        menu_html += '<li><a href="{}">{}</a>{}</li>'.format(item.get_absolute_url(), item.title, render_menu(item))
    menu_html += '</ul>'
    return menu_html
