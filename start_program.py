import subprocess

from processes import processes
from speaker import va_speak

STEAM_LINK = "start steam://rungameid/"


def start_pubg():

    try:
        subprocess.call(f"{STEAM_LINK}578080")
        va_speak("Запускаю пабг")
    except:
        va_speak('Не получилось запустить пубг')


def start_discord():
    try:
        subprocess.call('C:\\Users\\rredl\\AppData\\Local\\Discord\\Update.exe  --processStart Discord.exe')
        va_speak("Запускаю дискорд")
    except:
        va_speak('Не получилось запустить дискорд')


def start_steam():
    try:
        subprocess.call('D:\\Steam\\steam.exe')
        va_speak("Запускаю стим")
    except:
        va_speak('Не получилось запустить стим')