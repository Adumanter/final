import requests
from .models import TeleSettings
token = '1959986555:AAGChujSs93GCeFQyZrS3hYsQV6SSkruSDY'
chat_id = '-513112972'
text = 'Test_2'


def send_telegram():
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    a = text.find('{')
    b = text.find('}')
    c = text.rfind('{')
    d = text.rfind('}')

    part_1 = text[0:a]
    part_2 = text[b+1:c]
    part_3 = text[d:-1]

    text_slise = part_1 + part_2 + part_3

    reg = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slise
    })

