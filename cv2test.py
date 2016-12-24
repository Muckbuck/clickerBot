import cv2
import pyautogui

if(pyautogui.hotkey('ctrl', 'shift')):
    
    while True:
        k = cv2.waitKey(1) & 0xFF
        # press 'q' to exit
        if k == ord('q'):
            break
        elif k == ord('b'):
            print('b')
            # change a variable / do something ...
        elif k == ord('k'):
            print('k')
            # change a variable / do something ...
