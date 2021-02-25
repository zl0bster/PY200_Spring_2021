from typing import Optional, Iterator

from faker import Faker

from lesson_6.database_drivers import SqliteDB


class BookLibrary:
    DATABASE = 'library.sqlite3'
    BOOKS_TABLE = 'books'

    def __init__(self):
        self.__driver = SqliteDB(self.DATABASE)
        self.create_books_table()

    def create_books_table(self):
        sql = f"""
        CREATE TABLE IF NOT EXISTS {self.BOOKS_TABLE} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- первичный ключ, идентифицирует записи в таблице БД
            title TEXT NOT NULL, -- название книг не может быть пустым
            isbn13 TEXT UNIQUE NOT NULL, -- идентификатор книги не может повторяться
            pages INTEGER NOT NULL, -- количество страниц в книге не может быть пустым
            year INTEGER NOT NULL, -- год издания книги не может быть пустым
            price REAL NOT NULL, -- цена книги не может быть пустой
            discount INTEGER -- а вот скидка может быть пустой
        ); 
        """
        with self.__driver as cursor:  # использование менеджера контекста для выполнения запроса
            cursor.execute(sql)

    def insert_book(self, title: str, isbn13: str, pages: int, year: int, price: float,
                    discount: Optional[int] = None):
        sql = f"""
        INSERT INTO {self.BOOKS_TABLE}(
            title,
            isbn13,
            pages,
            year,
            price,
            discount
        )
        VALUES (?, ?, ?, ?, ?, ?);  -- оставляем заглушки в виде ?
        """
        with self.__driver as cursor:  # использование менеджера контекста для выполнения запроса
            cursor.execute(sql, [title, isbn13, pages, year, price, discount])

    @staticmethod
    def book_generator(count: int = 10) -> Iterator[tuple]:
        """

        (
            title: str,
            isbn13: str,
            pages: int,
            year: int,
            price: float,
            discount: Optional[int] = None
        )

        :param count: количество книг для случайной генерации
        :return: Кортеж с описанием книги
        """
        fake = Faker()

        for _ in range(count):
            fake_title = fake.pystr()
            fake_isbn13 = fake.isbn13()
            fake_page = fake.pyint(min_value=0, max_value=1000)
            fake_year = fake.pyint(min_value=1600, max_value=2021)
            fake_price = fake.pyfloat(min_value=0, max_value=10000, right_digits=2)
            fake_discount = fake.random_element([None, *range(10, 91, 10)])

            yield fake_title, fake_isbn13, fake_page, fake_year, fake_price, fake_discount

    def init_books(self, count):
        sql = f"""
        INSERT INTO {self.BOOKS_TABLE}(
            title,
            isbn13,
            pages,
            year,
            price,
            discount
        )
        VALUES (?, ?, ?, ?, ?, ?);  -- оставляем заглушки в виде ?
        """
        print('+'*10)
        print('init library')
        with self.__driver as cursor:  # использование менеджера контекста для выполнения запроса
            cursor.executemany(sql, self.book_generator(count))
            print(sql)

    def get_book_by_year(self, year: int) -> Iterator:
        sql = f"""
        SELECT *
        FROM {self.BOOKS_TABLE}
        WHERE year = {year};
        """

        with self.__driver as cursor:
            for row in list(cursor.execute(sql)):
                yield row

    def get_book_by_price_less(self, price: float):
        sql = f"""
        SELECT *
        FROM {self.BOOKS_TABLE}
        WHERE price < {price}
        ORDER BY year;
        """

        with self.__driver as cursor:
            return cursor.execute(sql).fetchall()

    def count_book_by_price_less(self, price: float):
        sql = f"""
        SELECT COUNT (*)
        FROM {self.BOOKS_TABLE}
        WHERE price < {price};
        """

        with self.__driver as cursor:
            return cursor.execute(sql).fetchone()

    def get_book_count(self):
        sql = f"""
        SELECT COUNT (*)
        FROM {self.BOOKS_TABLE};
        """
        with self.__driver as cursor:
            return cursor.execute(sql).fetchone()


if __name__ == '__main__':
    library = BookLibrary()
    # library.create_books_table()
    #
    # library.insert_book('test', '1221-3212-33', 20, 2020, 34.56)

    # for book in library.book_generator():
    #     print(book)

    # library.init_books(1000)

    # for book in library.get_book_by_year(2009):
    #     print(book)
    # list1 = library.get_book_by_price_less(1000)
    # for item in list1:
    #     print(item)
    print(f'\n', '+ ' *10, f'\n')
    obj1 = library.get_book_by_year(2010)
    for item in obj1:
        # next(library.get_book_by_year(2010))
        # item = next(obj1)
        print(item)

    print(f'\n', '+ ' *10, f'\n')
    limit = 400
    print(f'The number of books under {limit} is - {library.count_book_by_price_less(limit)} ')
    print(f'The total number of books is - {library.get_book_count()} ')
    # cntprs = library.count_book_by_price_less(limit)
    # print(f'The number of books under {limit} is - {cntprs} ')
    # cntall = library.get_book_count()
    # print(f'The total number of books is - {cntall} ')