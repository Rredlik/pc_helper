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
from processes import *
from start_program import *
from speaker import va_speak

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def greeting():
    va_speak("Привет, бро!")


def cancel():
    va_speak("Отдыхаю")



def check_name(voice: str):
    print(f"voice: {voice}")
    if voice.startswith(constants.BOT_NAME):

        cmd = recognize_cmd(filter_voice(voice))
        print(constants.COMMAND_DICT['commands'].keys())

        _command_ = cmd['cmd']

        print(_command_)


        if _command_ not in constants.COMMAND_DICT['commands'].keys():
            speaker.va_speak("Что?")
        else:
            globals()[_command_]()


def filter_voice(raw_voice: str):
    cmd = raw_voice

    for x in constants.BOT_NAME:
        cmd = cmd.replace(x, "").strip()

    for x in constants.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for command, text in constants.COMMAND_DICT['commands'].items():
        for x in text:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = command
                rc['percent'] = vrt
    return rc


if __name__ == '__main__':
    # va_speak("Привет, голосовой помошник Джарвис приступает к работе")
    print('start')
    listener.listen_test(check_name)
