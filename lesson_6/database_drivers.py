from abc import ABC, abstractmethod
import sqlite3


class DatabaseContextManager(ABC):
    @abstractmethod
    def __init__(self, db_driver, config: dict):
        self.__db_driver = db_driver
        self.config = config

    def __enter__(self):
        """Выполняет подключение к БД и возвращает курсор для выполнения SQL запросов."""
        print("Каждый раз при входе в контекстный менеджер создаем объект Connection и Cursor")
        self.conn = self.__db_driver.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Автоматически закрывает все соединения.
        В зависимости от успеха выполнения SQL запроса отменяет или применяет изменения.
        """
        print("Начинаем выход из контекстного менеджера ...")

        print("Закрываем курсор ...")
        self.cursor.close()
        if exc_type is not None:
            print("Если есть ошибки, то отменяем изменения в БД :((")
            self.conn.rollback()
        else:
            print("Если ошибок нет, то применяем изменения в БД :))")
            self.conn.commit()

        print("Закрываем соединение с БД!")
        self.conn.close()


class SqliteDB(DatabaseContextManager):
    DEFAULT_DATABASE = "db.sqlite3"
    DB_DRIVER = sqlite3

    def __init__(self, database=DEFAULT_DATABASE):
        config = {'database': database}
        super().__init__(self.DB_DRIVER, config)


class MysqlDB(DatabaseContextManager):
    ...


if __name__ == '__main__':
    db = SqliteDB()
    with db as cursor:
        print("-" * 20)
        print("Выполняем какие-то действия с БД")
        print("-" * 20)
