"""
    1. Реализовать класс JsonFileDriver, который будет описывать логику считывания (записи) элементов из (в) json файл.
    2. Реализовать класс SimpleFileDriver, который будет описывать логику считывания (записи) элементов из (в) файл.
    3. В блоке __main__ протестировать работу драйверов
"""

from typing import Sequence, Optional
from abc import ABC, abstractmethod
import os
import json


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class JsonFileDriver(IStructureDriver):
    def __init__(self, fileName: str, indent:Optional[int] = 4):
        self.fileName = fileName
        self.indent = indent

    def read(self) -> Sequence:
        if not os.path.exists(self.fileName):
            raise FileNotFoundError(self.fileName)
        with open(self.fileName, 'r') as jfile:
            result = json.load(fp=jfile)
        return result

    def write(self, data: Sequence) -> None:
        if os.path.exists(self.fileName):
            print(f'file {self.fileName} will be overwritten')
        data = [val for val in data]
        with open(self.fileName, 'w') as jfile:
            json.dump(data, jfile, indent=self.indent)


class SimpleFileDriver(IStructureDriver):
    def __init__(self, fileName: str):
        self.fileName = fileName

    def read(self) -> Sequence:
        if not os.path.exists(self.fileName):
            raise FileNotFoundError(self.fileName)
        with open(self.fileName, 'r') as tfile:
            result = tfile.readlines()
        # return result
        return [int(val) for val in result]

    def write(self, data: Sequence) -> None:
        if os.path.exists(self.fileName):
            print(f'file {self.fileName} will be overwritten')
        data = [val for val in data]
        with open(self.fileName, 'w') as tfile:
            tfile.writelines(data)


def main():
    sampleKeys = [i for i in range(13)]
    sampleDict = {key: str(key) for key in sampleKeys}
    print(sampleDict)
    driver = JsonFileDriver('tmp1.json')
    driver.write(sampleDict)
    result = driver.read()
    print(result)


if __name__ == '__main__':
    main()
