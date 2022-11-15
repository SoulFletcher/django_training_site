import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone, tg_text):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            a = text.find('{')
            b = text.find('}')
            m = text.find('{', b+1)
            g = text.find('}', b+1)
            c = text.rfind('{')

            part_1 = text[0:a]
            part_2 = text[b+1:m]
            part_3 = text[g+1:c]

            text_slice = part_1 + tg_name + part_2 + tg_phone + part_3 + tg_text
        else:
            text_slice = text
        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice,
                })
        except:
            pass

        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Всё хорошо. Сообщение отправлено!')
    else:
        pass

