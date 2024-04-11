from django.urls import NoReverseMatch, reverse


def get_full_url(url):
    try:
        print(f"{reverse(url)=}")
        return reverse(url)
    except NoReverseMatch:
        return url


def make_hierarchy(data: list[dict]) -> list[dict]:
    """Преобразует список словарей в иерархическую структуру."""
    # Создает словарь, где ключами будут id элементов, а значениями - сами
    # словари из списка
    id_dict = {item['id']: item for item in data}
    # Создает иерархический словарь, в который добавляем только те элементы, у
    # которых `parent_id` равно `None` (т.е. корневые элементы)
    hierarchy_dict = {
        item['id']: item for item in data if item['parent_id'] is None
    }
    for item in data:
        # Для каждого элемента создает пустой список детей
        item['children'] = []
        # Если у элемента есть родитель, добавляет его в список детей родителя
        if item['parent_id']:
            try:
                id_dict[item['parent_id']]['children'].append(item)
            except KeyError:
                print(
                    f"WARNING! Problem with adding child {item} "
                    f"to item with id={item['parent_id']}: "
                    "it appears this item does not exist in the current menu."
                )
    return list(hierarchy_dict.values())


def traverse_tree(tree: list[dict], func: callable) -> None:
    """Проходит по каждому элементу древовидной структуры и применяет к нему \
    указанную функцию.

    :param tree: Словарь, представляющих дерево.
    :param func: Функция, которую нужно применить к каждому элементу.
    """
    for item in tree:
        # Применяет функцию к текущему элементу
        func(item)
        # Если у элемента есть дети, рекурсивно применяет функцию к ним
        if 'children' in item and item['children']:
            traverse_tree(item['children'], func)


def enrich_with_open_attr(tree: list[dict], current_url: str) -> list[dict]:
    """Обогащает элементы древовидной структуры, устанавливая флаг 'open' для \
        определенных элементов.

    :param tree: Словарь, представляющий дерево.
    :param current_url: URL текущего элемента.
    :return: Обогащенное дерево.
    """
    # Создает словарь, который будет сопоставлять id каждого элемента со
    # ссылкой на сам элемент
    id_to_item = {}

    def initialize_item(item):
        # Устанавливает 'open' в False для всех элементов
        item.update(open=False)
        print(get_full_url(item.get("url")))
        item.update({
            "url": get_full_url(item.get("url")) or ""
        })
        # Заполняет словарь id_to_item
        id_to_item.update({item['id']: item})

    # Инициализирует все элементы дерева
    traverse_tree(tree, initialize_item)

    def process_item(item):
        # Если URL текущего элемента совпадает с current_url,
        # то обновляет 'open' для его родителей и детей первого уровня
        if item['url'] == current_url:
            # обновляет 'open' для текущего элемента
            item['open'] = True
            # # обновляет 'open' для детей первого уровня
            # for child in item['children']:
            #     print(child['url'])
            #     child['open'] = True
            # обновляет 'open' для родителей
            parent_id = item.get('parent_id')
            while parent_id is not None:
                parent = id_to_item.get(parent_id)
                if parent is not None:
                    parent['open'] = True
                    parent_id = parent.get('parent_id')
                else:
                    break

    # Применяет функцию process_item к каждому элементу дерева
    traverse_tree(tree, process_item)

    return tree
