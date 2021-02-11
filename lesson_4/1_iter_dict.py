"""
    Сделать свою реализацию словаря, в котором будет переопределен метод __iter__,
    чтобы он возвращал итератор не по ключам, а сразу по паре ключ, значение.

    Используйте наследование от встроеного типа dict, и полиморфизм для метода __iter__.
    Конструктор базового класса переопределять не нужно.

    Чтобы получить пары ключ-значение используйте либо метод базового self.items() либо
    функцию zip() для self.keys() и self.values()
"""

from typing import Iterator, Tuple, Hashable, Any


class MyDict(dict):  # ToDo Наследование от класса dict
    def __iter__(self) -> Iterator[Tuple[Hashable, Any]]:
        return iter(self.items())

    # def gen(self):
    #     for item_ in self.items():  # ToDo Переопределить метод. Данный
    #         print(item_)
    #         yield item_[0], item_[1]


if __name__ == '__main__':
    dict_ = MyDict({i: i * 3 for i in range(10)})
    for key, val in dict_:
        print(key, val)
    # for key in dict_:
    #     print('* ', key)
