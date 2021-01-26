def init(capacity_volume: int, occupied_volume: int) -> dict:
    """
    Создание и подготовка к работе объекта "Стакан"

    :param capacity_volume: Объем стакана
    :param occupied_volume: Объем занимаемой жидкости
    :return: Инициализированный словарь
    """
    ...


def is_glass(glass: dict) -> bool:
    """
    Функция которая проверяет является ли словарь стаканом

    :param glass: Объект стакан
    :return: Является ли объект стаканом или нет
    """
    ...


def add_water_to_glass(glass: dict, water: int) -> int:
    """
    Добавление воды в стакан.

    Если количество добавляемой жидкости превышает доступное место,
    то возвращается количество непоместившейся жидкости

    :param glass: Объект стакан
    :param water: Объем добавляемой жидкости
    :return: Объем непоместившейся жидкости
    """
    ...


def remove_water_from_glass(glass: dict, estimate_water: int) -> int:
    """
    Извлечение воды из стакана

    Если количество извлекаемой жидкости превышает количество воды в стакане,
    то возвращается реальное количество извлеченной воды

    :param glass: Объект стакан
    :param estimate_water: Объем извлекаемой жидкости
    :return: Объем реально извлеченной жидкости
    """
    ...


glass = {
    'capacity_volume': 500,
    'occupied_volume': 0,
    'is_glass': is_glass,  # функция проверки стакана
    'add_water_to_glass': add_water_to_glass,  # функция добавления воды
    'remove_water_from_glass': remove_water_from_glass,  # функция извлечения воды
}


if __name__ == '__main__':
    print(glass)
