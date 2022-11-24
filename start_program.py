import os

from processes import processes
from speaker import va_speak

STEAM_LINK = "start steam://rungameid/"


def start_pubg():

    try:
        os.system(f"{STEAM_LINK}578080")
    except:
        print('Error')


def start_discord():
    try:
        # print(processes())
        # if 'discord.exe' in ['element']:
        #     va_speak("Дискорд уже открыт")
        #     pass
        os.system('C:\\Users\\rredl\\AppData\\Local\\Discord\\Update.exe  --processStart Discord.exe')
        va_speak("Запускаю дискорд")

    except:
        print('Error')


def start_steam():
    try:
        os.system('D:\\Steam\\steam.exe')
        va_speak("Запускаю стим")

    except:
        print('Error')