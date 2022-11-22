import asyncio

import wmi
PRIORITY_PROGRAMS = {
    'programs': ['Calculator.exe']
}

f = wmi.WMI()


async def processes(priority_pr):
    for process in f.Win32_Process():
        if process.Name in PRIORITY_PROGRAMS['programs']:
            print(f'{process.ProcessID:<10} {process.Name}')




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
    asyncio.run(processes())

