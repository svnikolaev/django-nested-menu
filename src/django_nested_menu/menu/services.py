from menu.models import MenuItem
from menu.helpers import make_hierarchy, enrich_with_open_attr, traverse_tree


def get_hierarchical_menu(menu_name: str, current_url: str = None) -> dict:
    """Возвращает иерархическое меню с обогащенными атрибутами 'open'.

    :param menu_name: Имя меню.
    :param current_url: URL текущего элемента.
    :return: Иерархическое меню.
    """
    # Получает список элементов меню
    menu_items = list(MenuItem.objects.filter(menu_name=menu_name).values())

    # Если список элементов меню пустой - завершает выполнение
    if not menu_items:
        return {}

    # Преобразует список элементов в иерархическую структуру
    hierarchical_menu_items = make_hierarchy(menu_items)

    # Если указан текущий URL, обогащает элементы атрибутом 'open'
    if current_url:
        menu = enrich_with_open_attr(hierarchical_menu_items, current_url)
    else:
        # Если текущий URL не указан, то устанавливает 'open' в 'True' для
        # всех элементов
        menu = hierarchical_menu_items
        traverse_tree(
            menu,
            lambda item: item.update(open=True)
        )
    return menu
