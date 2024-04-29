import psycopg2
import alarm
import setting


class DatabaseConnection:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except Exception as ex:
            alarm.send_message_to_telegram_bot(ex)
        return False

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_val is not None:
            if bool(int(setting.settings.IN_PROD)):
                alarm.send_message_to_telegram_bot(exc_val)
            else:
                print("Database error: ", exc_type, exc_val, exc_tb)

        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
        return True
