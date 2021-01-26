class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости
        """
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def is_glass(self) -> bool:
        """
        Функция которая проверяет является ли словарь стаканом

        :return: Является ли объект стаканом или нет
        """
        ...

    def add_water_to_glass(self, water: int) -> int:
        """
        Добавление воды в стакан.

        Если количество добавляемой жидкости превышает доступное место,
        то возвращается количество непоместившейся жидкости

        :param water: Объем добавляемой жидкости
        :return: Объем непоместившейся жидкости
        """
        ...

    def remove_water_from_glass(self, estimate_water: int) -> int:
        """
        Извлечение воды из стакана

        Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается реальное количество извлеченной воды

        :param estimate_water: Объем извлекаемой жидкости
        :return: Объем реально извлеченной жидкости
        """
        ...


if __name__ == '__main__':
    glass = Glass(500, 0)
