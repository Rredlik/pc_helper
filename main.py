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
    main()
    # check_process()
    # # subprocess.process_exists('calculator.exe')
    # print('\n\n\n\n', processes)