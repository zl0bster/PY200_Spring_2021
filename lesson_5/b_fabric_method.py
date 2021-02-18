"""
Паттерн "Фабричный метод".
    1. Реализовать класс SimpleFileBuilder для построения драйвера SimpleFileDriver
    2. В блоке __main__ убедиться в построении драйверов JsonFileDriver и SimpleFileDriver
    3. В паттерне "Стратегия" использовать фабрику для получение драйверов в getter свойства driver.
        Getter должен возвращать драйвер, если его нет, то вызывать фабрику для получения драйвера.
"""

from abc import ABC, abstractmethod

from lesson_5.a_driver import IStructureDriver, JsonFileDriver, SimpleFileDriver


class DriverBuilder(ABC):
    @abstractmethod
    def build(self, filename: str):
        ...


class JsonFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.json'
    DEFAULT_INDENT = 4

    @classmethod
    def build(cls, filename) -> IStructureDriver:
        # filename = input('Введите название json файла: (.json)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.json'):
            filename = f'{filename}.json'

        return JsonFileDriver(filename)


class SimpleFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.txt'

    def build(self, filename) -> IStructureDriver:
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.txt'):
            filename = f'{filename}.txt'
        return SimpleFileDriver(filename)


class FabricDriverBuilder:
    DRIVER_BUILDER = {
        'json_file': JsonFileBuilder,
        'simple_file': SimpleFileBuilder
    }
    DEFAULT_DRIVER = 'json_file'

    @classmethod
    def get_driver(cls, filename=None):
        driver_name = input("Введите название драйвера: ")
        driver_name = driver_name or cls.DEFAULT_DRIVER

        driver_builder = cls.DRIVER_BUILDER[driver_name]
        return driver_builder.build(filename)


if __name__ == '__main__':
    driver = FabricDriverBuilder.get_driver()
