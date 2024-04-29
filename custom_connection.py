from session import DatabaseConnection
import setting


class MyProjectDatabaseConnection(DatabaseConnection):
    def __init__(self):
        super().__init__(dbname=setting.settings.dbname,
                         user=setting.settings.user,
                         password=setting.settings.password,
                         host=setting.settings.host,
                         port=setting.settings.port)

# add here your new class connection
