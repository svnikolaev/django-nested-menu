from django.core.management.base import BaseCommand
from menu.models import MenuItem

MENU_STRUCTURE = [
    {
        'menu_name': 'main_menu',
        'menu': [
            {
                'title': 'Home',
                'url': 'home',
                'children': [
                    {
                        'title': 'About',
                        'url': '/home/about'
                    },
                    {
                        'title': 'Contact',
                        'url': '/home/contact'
                    },
                    {
                        'title': 'Services',
                        'url': '/home/services',
                        'children': [
                            {
                                'title': 'Service 1',
                                'url': '/home/services/service-1'
                            },
                            {
                                'title': 'Service 2',
                                'url': '/home/services/service-2'
                            },
                            {
                                'title': 'Service 3',
                                'url': '/home/services/service-3'
                            }
                        ]
                    },
                    {
                        'title': 'Blog',
                        'url': '/home/blog',
                        'children': [
                            {
                                'title': 'Blog Post 1',
                                'url': '/home/blog/blog-post-1'
                            },
                            {
                                'title': 'Blog Post 2',
                                'url': '/home/blog/blog-post-2'
                            }
                        ]
                    }
                ]
            },
            {
                'title': 'Product 4',
                'url': '/products/product-4'
            },
        ]
    },
    {
        'menu_name': 'product_menu',
        'menu': [
            {
                'title': 'Products',
                'url': '/products',
                'children': [
                    {
                        'title': 'Product 1',
                        'url': '/products/product-1'
                    },
                    {
                        'title': 'Product 2',
                        'url': '/products/product-2'
                    },
                    {
                        'title': 'Product 3',
                        'url': '/products/product-3'
                    },
                    {
                        'title': 'Product 4',
                        'url': '/products/product-4'
                    },
                    {
                        'title': 'Product 5',
                        'url': '/products/product-5'
                    }
                ]
            }
        ]
    }
]


def create_menu_from_structure(
    menu_structure: list[dict],
    parent: MenuItem | None = None,
    menu_name: str | None = None
) -> None:
    """Создает структуру меню из списка элементов меню.

    Рекурсивно обрабатывает каждый элемент списка и его детей, если они есть.

    menu_structure: Список элементов меню.
    parent: Родительский элемент меню для текущего списка элементов.
    """
    for item in menu_structure:
        menu_item = MenuItem.objects.create(
            title=item['title'],
            url=item['url'],
            parent=parent,
            menu_name=item.get('menu_name', menu_name)
        )
        children = item.get('children', [])
        if children:
            create_menu_from_structure(children, menu_item,
                                       menu_name=menu_item.menu_name)


def create_menus_from_structure(menus_structure: list[dict]) -> None:
    """Создает структуру меню для каждого меню в списке.

    Передает каждый корневой узел функции create_menu_from_structure.

    menus_structure: Список меню.
    """
    for menu in menus_structure:
        menu_name = menu['menu_name']
        for root_node in menu['menu']:
            create_menu_from_structure([root_node], menu_name=menu_name)


class Command(BaseCommand):
    help = 'Создает структуру меню из списка'

    def handle(self, *args, **options):
        MenuItem.objects.all().delete()
        create_menus_from_structure(MENU_STRUCTURE)
