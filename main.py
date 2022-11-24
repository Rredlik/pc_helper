import listener
from speaker import va_speak
import constants
from browser import *
from processes import *
from start_program import *

from fuzzywuzzy import fuzz


def greeting():
    va_speak("Привет, бро!")


def cancel():
    va_speak("Отдыхаю")


def check_name(voice: str):
    # print(f"voice: {voice}")
    if voice.startswith(constants.BOT_NAME):

        cmd = recognize_cmd(filter_voice(voice))
        # print(constants.COMMAND_DICT['commands'].keys())
        # print(f'cmd: {cmd}')
        if cmd is None:
            return

        _command_ = cmd['cmd']

        # print(_command_)


        if _command_ not in constants.COMMAND_DICT['commands'].keys():
            va_speak("Что?")
        else:
            globals()[_command_]()


def filter_voice(raw_voice: str):
    cmd = raw_voice

    for x in constants.BOT_NAME:
        cmd = cmd.replace(x, "").strip()

    for x in constants.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    if cmd.startswith(constants.VA_REPEAT):
        cmd = cmd.replace(constants.VA_REPEAT, "", 1).strip()
        try:
            va_speak(cmd)
        except:
            va_speak('Нечего повторять')
        return 'none_command'

    return cmd



def recognize_cmd(cmd: str):
    if cmd == 'none_command':
        return
    rc = {'cmd': '', 'percent': 0}
    for command, text in constants.COMMAND_DICT['commands'].items():
        for x in text:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = command
                rc['percent'] = vrt
    return rc


if __name__ == '__main__':
    va_speak("Привет, голосовой помошник Джарвис приступает к работе")
    print('start')
    listener.listen_test(check_name)
