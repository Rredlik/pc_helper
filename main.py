import asyncio
import os
import subprocess
import speech_recognition
from fuzzywuzzy import fuzz
import datetime
# from num2t4ru import num2text
import webbrowser
import random


import listener
from browser import *
from processes import processes
from speaker import speak
from constants import COMMAND_DICT




sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def check_process():
    try:
        asyncio.run(processes())
        speak("Вывожу все работающие программы")
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
    speak("Привет, бро!")


def start_pubg():
    speak("Запускаю пубг")


def cancel():
    speak("Отдыхаю")


def va_respond(voice: str):
    print('va_respond')
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.COMMAND_DICT.keys():
            speaker.speak("Что?")
        else:
            print(globals())
            globals()[commands]()


def filter_cmd(raw_voice: str):
    print('filter_cmd')
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    print('recognize_cmd')
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc

def main():
    print('жду команду')
    query = listener.listen()
    print(f'query: {query}')
    # if query == 'остановись':
    #     return False
    for commands, text in COMMAND_DICT['commands'].items():
        print(f'text: {text}')
        if query in text:
            # print(f'commands: {commands}')
            globals()[commands]()



if __name__ == '__main__':
    print('start')
    listener.listen(va_respond())
    # check_process()
    # # subprocess.process_exists('calculator.exe')
    # print('\n\n\n\n', processes)