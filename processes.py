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
            cur_process = el.split(',')

            if len(cur_process) == 5:
                element = cur_process[0].replace('"', '').lower()
                element_pid = cur_process[1].replace('"', '')
                # print(f"element_pid: {element_pid} {element}\n")

                programs_in_work.append([element, element_pid])

                if element == close_program.lower():
                    print(f"Закрываю {element_pid} {element}\n")

                    subprocess.call(f"taskkill /pid {element_pid}")

    except exec() as er:

        print('Error: ', er)


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