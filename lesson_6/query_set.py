from lesson_6.database_drivers import SqliteDB


class QuerySet:
    def __init__(self, db_driver, from_, select='*', where='', order_by=''):
        self.db_driver = db_driver

        self.__select = select
        self.__from = from_
        self.__where = where
        self.__order_by = order_by

    def __str__(self):
        return self.sql

    @property
    def sql(self):
        """
        Примеры сформированных запросов

        SELECT * или SELECT field_1 или SELECT field_1, field_2, ...
        FROM table_name
        WHERE condition_1 = value_1 или WHERE condition_1 = value_1 AND condition_2 = value_2 ...
        ORDER BY field_1 или ORDER BY field_1 DESC
        """
        sql = f"SELECT {self.__select}\n"
        sql += f"FROM {self.__from}\n"

        if self.__where:
            sql += f"{self.__where}\n"

        if self.__order_by:
            sql += f"{self.__order_by}\n"

        return sql

    @property
    def rows(self):
        with self.db_driver as cursor:
            return cursor.execute(self.sql).fetchall()

    def list_values(self, *args) -> 'QuerySet':
        select = '*' if not args else ', '.join(map(str, args))
        return QuerySet(self.db_driver, self.__from, select=select, where=self.__where, order_by=self.__order_by)

    def order_by(self, column, reverse=False) -> "QuerySet":
        order_by = f"ORDER BY {column}"
        if reverse:
            order_by += " DESC"

        return QuerySet(self.db_driver, self.__from, select=self.__select, where=self.__where, order_by=order_by)

    def filter(self, **kwargs) -> 'QuerySet':
        """Фильтрация запроса по полям"""
        condition = ' AND\n\t'.join(f"{field} = {value}" for field, value in kwargs.items())

        key_word = "WHERE " if not self.__where else " AND\n\t"
        self.__where += f"{key_word}{condition}"

        return QuerySet(self.db_driver, self.__from, where=self.__where, order_by=self.__order_by)

    @staticmethod
    def prepare_condition(**kwargs) -> str:
        operators = {
            '__gt': '>',
            '__gte': '>=',
            '__lt': '<',
            '__lte': '<=',
        }
        parse_condition = ...

        return parse_condition


if __name__ == '__main__':
    driver = SqliteDB('library.sqlite3')
    print(QuerySet(driver, 'books').order_by('year', True).filter(test=1))

    # qs = QuerySet(driver, 'books').filter(year=4, title='czs').filter(extend=100, test=2).list_values('test')
    # print(qs)

