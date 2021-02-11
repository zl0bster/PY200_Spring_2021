from typing import Any, Sequence, Optional
from a2_linked_list_VP import LinkedList

"""
Двусвязный список на основе односвязного списка.

    Самостоятельное задание. В двусвязном списке должны быть следующие методы:
    - **`__str__`**
    - **`__repr__`**
    - **`__getitem__`**
    - **`__setitem__`**
    - **`__len__`**
    - **`insert`**
    - **`index`**
    - **`remove`**
    - **`append`**
    - **`__iter__`**

    Необязательно все эти методы должны быть переопределены в явном виде. По максимуму используйте
    наследование, если поведение списков в контексте реализации указанных метод схоже.
    С точки зрения наследования по минимуму перегружайте методы. При необходимости рефакторите базовый класс,
    чтобы локализовать части кода во вспомогательные функции, которые имеют различное поведение
    в связном и двусвязном списках.
    Стремитесь к минимизации кода в дочернем классе.

    Есть какой-то метод класса DoubleLinkedList хотите отработать в явном виде ещё раз, не возбраняется.
"""


# ToDo импорт любой вашей реалиазации LinkedList


class DoubleLinkedList(LinkedList):
    class DoubleLinkedNode(LinkedList.Node):
        def __init__(self, value: Any, next_: Optional['DoubleLinkedNode'] = None,
                     prev_: Optional['DoubleLinkedNode'] = None):
            super().__init__(value=value, next_=next_)
            self.prev = prev_

        @property
        def prev(self):
            return self.__prev

        @prev.setter
        def prev(self, prev_: Optional['DoubleLinkedNode']):
            if not isinstance(prev_, self.__class__) and prev_ is not None:
                msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                      f"или None, не {prev_.__class__.__name__}"
                raise TypeError(msg)
            self.__prev = prev_

        def __repr__(self):
            """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
            return f"DoubleLinkedNode({self.value}, {self.next}, {self.prev})"

    def __init__(self, data: Sequence = None):
        super().__init__(data)
        self.__len = 0

    def __repr__(self):
        return f"DoubleLinkedList({str(self)})"

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        appendNode = self.DoubleLinkedNode(value)
        if self.head is None:
            self.head = appendNode
        else:
            appendNode.prev = self.tail
            self.tail.next = appendNode
        self.tail = appendNode
        self._len += 1
        print(self._len)


if __name__ == '__main__':
    ll2 = DoubleLinkedList(range(30))
    print(ll2)
    print(len(ll2))
    print(repr(ll2))
    ll3 = repr(ll2)
    print(ll3)
    print(len(ll3))
