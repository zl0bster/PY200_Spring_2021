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
            # self.next(next_)

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

    def __init__(self, data: Sequence = None):
        """Конструктор связного списка"""
        self.__len = 0
        self.head = None  # Node
        self.tail = None
        if data:  # ToDo Проверить, что объект итерируемый. Метод self.is_iterable
            if not hasattr(data, "__iter__"):
                self.append(data)
                return
            for value in data:
                self.append(value)

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head: Node):
        """Setter проверяет и устанавливает следующий узел связного списка"""
        if not isinstance(head, self.Node) and head is not None:
            msg = f"Устанавливаемое значение должно быть экземпляром класса {self.Node} " \
                  f"или None, не {head.__class__.__name__}"
            raise TypeError(msg)
        self.__head = head

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, tail: Node):
        """Setter проверяет и устанавливает следующий узел связного списка"""
        if not isinstance(tail, self.Node) and tail is not None:
            msg = f"Устанавливаемое значение должно быть экземпляром класса {self.Node} " \
                  f"или None, не {tail.__class__.__name__}"
            raise TypeError(msg)
        self.__tail = tail

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        result = ""
        separator = "; "
        for current_node in self.__list_iteration():
            result += str(current_node.value)
            if not (current_node.next is None):
                result += separator
        return result

    def __list_iteration(self):
        current_node = self.head
        for _ in range(self.__len):
            yield current_node
            current_node = current_node.next
        return

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f"LinkedList({[val for val in self]})"

    def __len__(self):
        return self.__len

    def __check_index(self, index: int):
        if type(index) != int:
            raise TypeError
        if not (0 <= index < self.__len):
            raise IndexError

    def __step_by_step(self, index: int) -> Node:
        self.__check_index(index=index)
        currentNode = self.head
        for _ in range(index):
            currentNode = currentNode.next
        return currentNode

    def __getitem__(self, item: int) -> Any:
        currentNode = self.__step_by_step(index=item)
        return currentNode.value

    def __setitem__(self, key, value):
        currentNode = self.__step_by_step(key)
        currentNode.value = value

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        append_node = self.Node(value)
        if self.head is None:
            self.head = append_node
        else:
            # tail = self.head
            # for _ in range(self.len_ - 1):
            #     tail = tail.next
            # self.__linked_nodes(tail, append_node)
            self.tail.next = append_node
        self.tail = append_node
        self.__len += 1

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def to_list(self) -> list:
        return [value for value in self]

    def insert(self, index: int, value: Any) -> None:
        # if
        if index == 0:
            currentNode = self.head
            newNode = self.Node(value=value, next_=currentNode)
            self.head = newNode
        elif 0 <= index < (self.__len - 1):
            currentNode = self.__step_by_step(index=index)
            newNode = self.Node(value=value, next_=currentNode.next)
            currentNode.next = newNode
        elif index == (self.__len - 1):
            currentNode = self.tail
            newNode = self.Node(value=value)
            currentNode.next = newNode
            self.tail = newNode
        else:
            raise IndexError
        self.__len += 1

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.__len = 0

    def index(self, value: Any) -> int:
        ...

    def remove(self, value: Any) -> None:
        lastNode = self.head
        for current_node in self.__list_iteration():
            if value == current_node.value:
                if current_node == self.head:
                    self.head = current_node.next
                elif current_node == self.tail:
                    self.tail = lastNode
                    lastNode.next = None
                else:
                    lastNode.next = current_node.next
                self.__len -= 1
                current_node.next = None
                return
            lastNode = current_node
        raise ValueError

    def sort(self) -> None:
        ...

    def is_iterable(self, data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        return hasattr(data, "__iter__")

    def __contains__(self, item: Any):
        return any(item == value for value in self)


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4])
    print(ll)
    print(ll[2])
    # print(ll[-2])
    # print(ll["a"])
    for val in ll:
        print(val)
    ll.append(18)
    # ll.append(**(l for l in range(5)))
    print(f"length = {len(ll)} !")
    print(ll.to_list())
    print(4 in ll)
    print(0 in ll)
    print('*' * 10)
    ll2 = repr(ll)
    print(ll2)
    ll.insert(2, 12)
    print(ll)
    ll.insert(0, 13)
    print(ll)
    ll.insert(len(ll) - 1, 11)
    print(ll)
    # ll.insert(-2, 13)
    print('*' * 10)
    ll.remove(11)
    ll.remove(1)
    # ll.head = 0
    print(ll)
    ll.clear()
    print(ll)
    ll2 = LinkedList(1)
    print(ll2)
