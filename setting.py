from pydantic import BaseSettings

from dotenv import load_dotenv

from os import environ

load_dotenv()


class Settings(BaseSettings):
    dbname: str = environ.get('DBNAME', 'postgres')
    user: str = environ.get('USER', 'postgres')
    password: str = environ.get('PASSWORD', '')
    host: str = environ.get('HOST', 'localhost')
    port: str = environ.get('PORT', '5432')
    bot_url: str = environ.get('BOT_URL', '')
    telegram_chat_id: str = environ.get('CHAT_ID', '')
    IN_PROD: str = environ.get('IN_PROD', '0')


settings = Settings()
