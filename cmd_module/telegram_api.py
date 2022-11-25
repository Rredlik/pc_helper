import requests

from cmd_module import constants
from va_module.speaker import va_speak

token = "5937099005:AAEU71aOTYvzxW_3f7wtNhMXbPiaPzN3flw"
url = "https://api.telegram.org/bot"
channel_id = "@Djarvis_va_bot"
url += token
method = url + "/sendMessage"
chat_id = '351931465'


def send_telegram(text: str):
    try:
        print(text)
        print(constants.COMMAND_DICT['commands']['send_telegram'])
        for comm in constants.COMMAND_DICT['commands']['send_telegram']:
            if text.startswith(comm):
                print(text)
                cmd = text.replace(comm, "", 1).strip()

                print(cmd)
                try:
                    va_speak(cmd)
                    r = requests.post(method, data={
                        "chat_id": chat_id,
                        "text": text
                    })

                    if r.status_code != 200:
                        va_speak('Сообщение не отправилось')

                    return
                except:
                    va_speak('Нечего повторять')

    except:
        va_speak('Сообщение не отправилось')

if __name__ == '__main__':
  send_telegram("hello world!")