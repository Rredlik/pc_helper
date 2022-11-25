from fuzzywuzzy import fuzz

from va_module import listener
from va_module.speaker import va_speak
from cmd_module import constants
from cmd_module.processes import *
from cmd_module.start_program import *
from cmd_module.browser import *
from cmd_module.telegram_api import *



def greeting():
    va_speak("Привет, бро!")


def cancel():
    va_speak("Отдыхаю")


def check_name(voice: str):
    print(f"voice: {voice}")
    if voice.startswith(constants.BOT_NAME):
        raw_voice = filter_voice(voice)
        cmd = recognize_cmd(raw_voice)
        # print(constants.COMMAND_DICT['commands'].keys())
        # print(f'cmd: {cmd}')
        if cmd is None:
            return

        _command_ = cmd['cmd']

        # print(_command_)

        if _command_ not in constants.COMMAND_DICT['commands'].keys():
            va_speak("Что?")
        else:
            try:
                globals()[_command_]()
            except TypeError:
                globals()[_command_](raw_voice)



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
