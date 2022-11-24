import os
import subprocess

from constants import BROWTHER_PATH
from speaker import va_speak


def start_browser():
    try:
        va_speak("Запускаю браузер")
        os.system(f'start {BROWTHER_PATH}')
    except:
        print('Error')


def start_vkcom():
    try:
        os.system(f'{BROWTHER_PATH} vk.com')
        va_speak("Запускаю vk.com")
    except:
        print('Error')