import msvcrt
from msvcrt import getch

while(True):
    
    if msvcrt.kbhit() and ord(msvcrt.getch()) == 27:
        print('hi')
        break
