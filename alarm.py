import requests
from datetime import datetime
from setting import settings


def send_message_to_telegram_bot(message):
    telegram_url = 'https://api.telegram.org/'
    token = settings.bot_url
    chat_id = settings.telegram_chat_id
    url = f'{telegram_url}{token}/sendMessage?chat_id={chat_id}&parse_mode=html&text={message}'
    response = requests.get(url, verify=False)
    message_id = response.json()['result']['message_id']
    print('message_id', message_id, 'status_code', response.status_code, 'response', response.json(), 'date', datetime.now())


