import psycopg2
from .setting import settings


class DatabaseConnection:
    def __init__(self):
        self.dbname = settings.dbname
        self.user = settings.user
        self.password = settings.password
        self.host = settings.host
        self.port = settings.port

        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
        return False
