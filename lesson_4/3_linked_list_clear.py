"""
    Взять класс LinkedList и определить для него соответвующие методы очистки списка от объектов Node.

    1. Перегрузить в классе Node метод __del__, чтобы видеть сообщение о том, что текущий объект удален
    2. Используя встроенную функцию sys.getrefcount() от каждого узла списка получить информацию о количестве
        переменных, которые ссылаются на данный объект. Прокоментировать и рассказать откуда берется каждая ссылка.
        см. Алгоритм подсчета ссылок https://colab.research.google.com/drive/12UErjm9lm31DPEFSxcyrH47LUX5oRwyH#scrollTo=jxYLDA_KDPv6
    3. Реализовать метод **`clear`**. Метод очиски связанного списка должен быть оформлен в одну строку с
        удалением всех узлов списка.
"""

import sys
from typing import Any, Sequence, Optional


class LinkedList:
    class Node:
        """
        Внутренний класс, класса LinkedList.

        Пользователь напрямую не работает с узлами списка, узлами оперирует список.
        """

        def __init__(self, value: Any, next_: Optional['Node'] = None):
            """
            Создаем новый узел для односвязного списка

            :param value: Любое значение, которое помещено в узел
            :param next_: следующий узел, если он есть
            """
            self.value = value
            self.next = next_  # Вызывается сеттер

        @property
        def next(self):
            """Getter возвращает следующий узел связного списка"""
            return self.__next

        @next.setter
        def next(self, next_: Optional['Node']):
            """Setter проверяет и устанавливает следующий узел связного списка"""
            if not isinstance(next_, self.__class__) and next_ is not None:
                msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                      f"или None, не {next_.__class__.__name__}"
                raise TypeError(msg)
            self.__next = next_

        def __repr__(self):
            """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
            return f"Node({self.value}, {self.next})"

        def __str__(self):
            """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
            return f"{self.value}"

        def __del__(self):  # ToDo Вывод сообщения о том, что узел был удален
            ...

    def __init__(self, data: Sequence = None):
        """Конструктор связного списка"""
        self.__len = 0
        self.head = None  # Node

        if data:
            for value in data:
                self.append(value)

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        return f"{[value for value in self]}"

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f"{type(self).__name__}({[value for value in self]})"

    def __len__(self) -> int:
        print("Вызван метод __len__ класса LinkedList")
        return self.__len

    def __step_by_step_on_nodes(self, index) -> 'Node':
        """Перемещение по узлам"""
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.__len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, item: int) -> Any:
        print('Вызван метод __getitem__')
        current_node = self.__step_by_step_on_nodes(item)
        return current_node.value

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        append_node = self.Node(value)
        if self.head is None:
            self.head = append_node
        else:
            tail = self.head  # ToDo Завести атрибут self.tail, который будет хранить последний узел
            for _ in range(self.__len - 1):
                tail = tail.next
            self.__linked_nodes(tail, append_node)
        self.__len += 1

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def clear(self):  # ToDo перегрузить метод для удаления всех узлов
        ...


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4, 5])
    print(sys.getrefcount(ll))

    # ToDo Вывести количество ссылок на каждый узел списка
    ...

    ll.clear()
