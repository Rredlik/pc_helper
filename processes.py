import asyncio
import os
import subprocess

import wmi
PRIORITY_PROGRAMS = ['Calculator.exe']

f = wmi.WMI()


async def processes():
    for process in f.Win32_Process():
        if process.Name in PRIORITY_PROGRAMS:
            print(f'{process.ProcessID:<10} {process.Name}')


def start_browser(close_program):
    programs_in_work = []
    try:
        _procces = subprocess.check_output("tasklist /fo csv /nh")
        _procces = str(_procces).split('\\r\\n')

        for el in _procces:
            element = el.split(',')[0].replace('"', '')
            programs_in_work.append(element)
            if element == close_program:
                print(f"Закрываю программу {close_program}")

    except:

        print('Error')


# async def processes():
#     pr = []
#     for process in f.Win32_Process():
#         pr.append(process.Name)
#     pr.sort()
#     for el in pr:
#         print(el)
#         if el in PRIORITY_PROGRAMS['programs']:
#             print(f'######## {el} ########')

if __name__ == '__main__':
    # asyncio.run(processes())
    # print(start_browser)
    # for my_computer in f:
    #     print(my_computer)
    prog = input()
    start_browser(prog)



'tasklist /v /fo list /nh > Процессы.csv'