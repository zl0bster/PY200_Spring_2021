from typing import Any, Sequence, Optional


class LinkedList:
    class Node:
        def __init__(self, value: Any, next_: 'Node' = None):
            """
            Создаем новый узел для односвязного списка

            :param value:
            :param next_: node class Node
            """
            ...

        @property
        def next(self):
            ...

        @next.setter
        def next(self, next_: 'Node'):
            ...

        def __str__(self):
            ...

        def __repr__(self):
            ...

    def __init__(self, data: Sequence = None):
        ...

    def is_iterable(self, data):
        ...

    def append(self, value):
        ...

    def linked_nodes(self, left: Optional[Node], right: Optional[Node]):
        ...

    def insert(self, index: int, value: Any):
        ...

    def find(self, value):
        ...

    def remove(self, value):
        ...

    def len(self):
        ...

    def __getitem__(self, item: int) -> Any:
        ...

    def __setitem__(self, key, value):
        ...

    def __delitem__(self, key):
        ...

    def clear(self):
        ...

    def str(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""

    def to_list(self):
        ...

    def sort(self):
        ...
