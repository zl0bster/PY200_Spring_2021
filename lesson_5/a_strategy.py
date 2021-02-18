"""
Реализовать класс LinkedListWithDriver от класса LinkedList.
Дочерний класс должен уметь работать с реализованными ранее драйверами.

    1. Реализовать свойство driver, которое будет возвращать используемый драйвер и проверять, что устанавливаемый
        драйвер является экземпляром класса IStructureDriver.
    2. Реализовать метод read, который с помощью встроенного драйвера будет получать последовательность элементов и
        помещать их в самого себя. При вызове метода связанный список должен полностью перезаписываться новыми элементами.
    3. Реализовать метод write, который передавать последовательность элементов для записи драйвером.
    4. Протестировать паттерн "Стратегия" в ключе независимости работы экземляров LinkedListWithDriver от драйверов
        IStructureDriver. LinkedListWithDriver должен уметь работать со всеми экземплярами дочерних классов класс IStructureDriver.
    5. LinkedListWithDriver должен поддерживать "горячую замену" драйвера, то есть без удаления и создания нового
        экземпляра LinkedListWithDriver, а замена драйвера существующего экземпляра.
"""

from lesson_5.a_linkedlist import LinkedList
from lesson_5.a_driver import IStructureDriver, JsonFileDriver, SimpleFileDriver
from lesson_5.b_fabric_method import FabricDriverBuilder


class LinkedListWithDriver(LinkedList):
    def __init__(self, data, driver: IStructureDriver = None):
        # ToDo вызвать конструктор базового класса LinkedList
        super().__init__(data)
        self.__driver = driver

    @property
    def driver(self):
        if self.__driver is None:
            self.__driver = FabricDriverBuilder.get_driver()
        return self.__driver

    @driver.setter
    def driver(self, driver):
        self.__driver = driver

    def read(self):
        """Взять драйвер и считать из него информацию в LinkedList"""
        seq = self.__driver.read()
        self.clear()
        for item in seq:
            self.append(item)

    def write(self):
        """Взять драйвер и записать в него информацию из LinkedList"""
        # seq = [i for i in self.]
        self.__driver.write(self)


if __name__ == '__main__':
    sampleSeq=[i for i in range(13)]
    # driver = JsonFileDriver('tmp2.json')
    # ll = LinkedListWithDriver([1, 2, 3, 4, 5], driver)
    ll = LinkedListWithDriver('')
    print(ll.driver)
    print(ll)

    ll.driver = SimpleFileDriver('tmp.txt')
    ll.read()
    print(ll)
    ll.driver = JsonFileDriver('tmp3.json')
    ll.write()
