import asyncio
import os
import subprocess
import speech_recognition

from browser import *
from processes import processes
from speaker import speak
from constants import commands_dict


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def check_process():
    try:
        asyncio.run(processes())
        speak("Вывожу все работающие программы")
    except:
        print('Error')


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        speak("Неизвестная комманда")


def greeting():
    speak("Привет, бро!")


def start_pubg():
    speak("Запускаю пубг")


def cancel():
    speak("Отдыхаю")


def main():
    print('жду команду')
    query = listen_command()
    print(f'query: {query}')
    # if query == 'остановись':
    #     return False
    for commands, text in commands_dict['commands'].items():
        # print(f'text: {text}')
        if query in text:
            # print(f'commands: {commands}')
            globals()[commands]()


if __name__ == "__main__":
    cycle = True
    while cycle:
        cycle = main()
