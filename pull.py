from setting import settings
from psycopg2 import pool


class DatabaseConnectionPull:
    # Объявляем статический атрибут connection_pool и инициализируем его значением None
    connection_pool = None

    def __init__(self):
        self.dbname = settings.dbname
        self.user = settings.user
        self.password = settings.password
        self.host = settings.host
        self.port = settings.port
        if DatabaseConnectionPull.connection_pool is None:
            DatabaseConnectionPull.connection_pool = pool.SimpleConnectionPool(
                minconn=1,  # Минимальное количество соединений в пуле
                maxconn=10,  # Максимальное количество соединений в пуле
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )

        self.connection = None
        self.cursor = None

    def __enter__(self):
        # Получаем соединение из пула
        self.connection = DatabaseConnectionPull.connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Закрываем курсор
        if self.cursor is not None:
            self.cursor.close()

        # Возвращаем соединение в пул
        if self.connection is not None:
            DatabaseConnectionPull.connection_pool.putconn(self.connection)

        # Если возникло исключение, возвращаем False, чтобы исключение не подавлялось
        return False
