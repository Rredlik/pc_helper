import asyncio

import wmi
PRIORITY_PROGRAMS = ['Calculator.exe']

f = wmi.WMI()


async def processes():
    for process in f.Win32_Process():
        if process.Name in PRIORITY_PROGRAMS:
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
    # asyncio.run(processes())
    print(f)
    # for my_computer in f:
    #     print(my_computer)



