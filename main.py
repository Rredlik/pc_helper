import asyncio
import os
import subprocess

from browser import *
from processes import processes
from speaker import speak





def check_process():
    try:
        asyncio.run(processes())
        speak("Вывожу все работающие программы")
    except:
        print('Error')



def main():
    query = input()
    if query == 'браузер':
        start_browser()
    elif query == 'открой вк' or 'вк':
        start_vkcom()


if __name__ == '__main__':
    # main()
    check_process()
    # # subprocess.process_exists('calculator.exe')
    # print('\n\n\n\n', processes)

import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    # 'main_command':{
    #     ['']
    # },
    'commands': {
        'cancel': ['отмена комманды', 'отмена', 'не слушай', 'отдыхай'],
        'greeting': ['привет', 'здравствуй', 'запуск'],
        'start_pubg': ['запусти pubg', 'запусти плеер анонс батлграунд', 'запусти плеер анонс battleground'],
        'parting': ['пока', 'до свидания', 'выключение']
    }
}


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return "Неизвестная комманда"


def greeting():
    print("Привет, бро!")


def start_pubg():
    print("Запускаю пубг")


def cancel():
    print("Отдыхаю")


def main():
    query = listen_command()
    print(f'query: {query}')
    for commands, text in commands_dict['commands'].items():
        print(f'text: {text}')
        if query in commands:
            print(f'commands: {commands}')
            globals()[commands]()
            break


if __name__ == "__main__":
    main()
