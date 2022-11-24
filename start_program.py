import os

STEAM_LINK = "start steam://rungameid/"


def start_pubg():

    try:
        os.system(f"{STEAM_LINK}578080")
    except:
        print('Error')
