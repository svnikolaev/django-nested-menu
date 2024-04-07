from typing import Dict, Optional

from django.core.management.base import BaseCommand
from pages.models import Page

PAGES_STRUCTURE = {
    'Home': {
        'slug': 'home',
        'content': 'This is the home page.',
        'children': {
            'About': {
                'slug': 'about',
                'content': 'This is the about page.',
                'children': {}
            },
            'Contact': {
                'slug': 'contact',
                'content': 'This is the contact page.',
                'children': {}
            },
            'Services': {
                'slug': 'services',
                'content': 'This is the services page.',
                'children': {
                    'Service 1': {
                        'slug': 'service-1',
                        'content': 'This is the page for service 1.',
                        'children': {}
                    },
                    'Service 2': {
                        'slug': 'service-2',
                        'content': 'This is the page for service 2.',
                        'children': {}
                    }
                }
            }
        }
    },
    'Products': {
        'slug': 'products',
        'content': 'This is the products page.',
        'children': {
            'Product 1': {
                'slug': 'product-1',
                'content': 'This is the page for product 1.',
                'children': {}
            },
            'Product 2': {
                'slug': 'product-2',
                'content': 'This is the page for product 2.',
                'children': {}
            },
            'Product 3': {
                'slug': 'product-3',
                'content': 'This is the page for product 3.',
                'children': {}
            }
        }
    }
}


def create_pages_from_structure(
    structure: Dict[str, Dict[str, str]],
    parent: Optional[Page] = None,
    parent_path: str = ''
) -> None:
    """Рекурсивно создает страницы на основе вложенной структуры.

    :param structure: словарь с данными страниц
    :param parent: родительская страница для текущей структуры
    :param parent_path: путь родительской страницы
    """
    for title, page_data in structure.items():
        # Объединяет путь родителя и slug текущей страницы, если родитель
        # существует, иначе использует slug текущей страницы
        slug = page_data['slug']
        path = (
            parent_path + '/' + slug
            if parent_path
            else slug
        )
        # Попытаться получить страницу или создать, если ее не существует
        page, created = Page.objects.get_or_create(
            title=title,
            defaults={
                'content': page_data['content'],
                'parent': parent,
                'slug': slug,
                'path': path
            }
        )
        # Если страница уже существует, обновляем ее данные
        if not created:
            page.content = page_data['content']
            page.parent = parent
            page.slug = slug
            page.path = path
            page.save()
        # Рекурсивно создаём дочерние страницы
        create_pages_from_structure(
            page_data['children'], parent=page, parent_path=path
        )


class Command(BaseCommand):
    help = 'Generate pages from the PAGES_STRUCTURE'

    def handle(self, *args, **options):
        # Создать страницы на основе PAGES_STRUCTURE
        create_pages_from_structure(PAGES_STRUCTURE)
        self.stdout.write(self.style.SUCCESS('Successfully generated pages'))
