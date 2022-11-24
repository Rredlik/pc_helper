import asyncio
import speech_recognition
from fuzzywuzzy import fuzz
import datetime
# from num2t4ru import num2text
import webbrowser
import random

import constants
import listener
import speaker
from browser import *
from processes import processes
from speaker import va_speak
from constants import COMMAND_DICT

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def check_process():
    try:
        asyncio.run(processes())
        va_speak("Вывожу все работающие программы")
    except:
        print('Error')


# def listen_command():
#     try:
#         with speech_recognition.Microphone() as mic:
#             sr.adjust_for_ambient_noise(source=mic, duration=0.5)
#             audio = sr.listen(source=mic)
#             query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
#         return query
#     except speech_recognition.UnknownValueError:
#         speak("Неизвестная комманда")


def greeting():
    va_speak("Привет, бро!")


def cancel():
    va_speak("Отдыхаю")


def va_respond(voice: str):
    print('va_respond')
    print(voice)
    if voice.startswith(constants.COMMAND_DICT):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in constants.COMMAND_DICT.keys():
            speaker.va_speak("Что?")
        else:
            print(globals())
            # globals()[commands]()


def filter_cmd(raw_voice: str):
    print('filter_cmd')
    cmd = raw_voice

    for x in constants.BOT_NAME:
        cmd = cmd.replace(x, "").strip()

    # for x in config.VA_TBR:
    #     cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    print('recognize_cmd')
    rc = {'cmd': '', 'percent': 0}
    for command, text in constants.COMMAND_DICT.items():

        for x in text:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = command
                rc['percent'] = vrt

    return rc


print('start')
print(f'globals: {globals()}')
if __name__ == '__main__':
    print('start')

    va_speak("Привет, голосовой помошник Джарвис приступает к работе")

    listener.listen_test()
