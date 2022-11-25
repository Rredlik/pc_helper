import asyncio
import subprocess
import wmi

from va_module.speaker import va_speak

PRIORITY_PROGRAMS = ['Calculator.exe']

f = wmi.WMI()

def check_process():
    try:
        asyncio.run(processes())
        va_speak("Вывожу все работающие программы")
    except:
        print('Error')


def processes_slow():
    for process in f.Win32_Process():
        if process.Name in PRIORITY_PROGRAMS:
            print(f'{process.ProcessID:<10} {process.Name}')


def processes(close_program=None):
    """

    :param close_program: if you want to close some write it's 'name.exe'
    """
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


                if not close_program is None:
                    if element == close_program.lower():
                        print(f"Закрываю {element_pid} {element}\n")

                        subprocess.call(f"taskkill /pid {element_pid}")

        if close_program is None:
            return programs_in_work

    except exec() as er:

        print('Error: ', er)


def sleep_windows():
    try:
        subprocess.call("Rundll32.exe user32.dll, LockWorkStation")
    except:
        va_speak('Не получилось заблокировать экран')

if __name__ == '__main__':

    # prog = input()
    print(processes())



'tasklist /v /fo list /nh > Процессы.csv'