import os
import subprocess

from constants import BROWTHER_PATH
from speaker import speak


def start_browser():
    try:
        os.system(f'start {BROWTHER_PATH}')
        speak("Запускаю браузер")
    except:
        print('Error')


def start_vkcom():
    try:
        os.system(f'{BROWTHER_PATH} vk.com')
        speak("Запускаю vk.com")
    except:
        print('Error')