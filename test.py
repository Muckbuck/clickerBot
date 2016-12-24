import pyautogui 
import json
import os
import ast
from msvcrt import getch
import msvcrt
import time
import cv2
import pyHook
import pythoncom

screenWidth, screenHeight = pyautogui.size() 

def mouse(x, y):
    pyautogui.moveTo(300, 200)

def storeProfile():
    posList = {'Positions': []}
    
    profileName = pyautogui.prompt('Profile Name: ') 
    while True:  
        
        if msvcrt.kbhit() and ord(msvcrt.getch()) == 13:
            break     

                
                
    while True:
        print('Recording process started')

        def onclick(event):
            mouseClickPos =  str(event.Position)
            mouseClickList = mouseClickPos.split(',')
            mouseClickPos0 = mouseClickList[0]
            mouseClickPos1 = mouseClickList[1]
            mouseClickPos0String = str(mouseClickPos0)
            mouseClickPos1String = str(mouseClickPos1)
            x = mouseClickPos0.translate(None, '(')
            y = mouseClickPos1.translate(None, ')')
            posList['Positions'].append({'xPos': x, 'yPos': y})
            print x
            print y
            print posList

            return True

        hm = pyHook.HookManager()
        hm.SubscribeMouseAllButtonsDown(onclick)
        hm.HookMouse()
        pythoncom.PumpMessages()
        hm.UnhookMouse()
                        
        if msvcrt.kbhit() and ord(msvcrt.getch()) == 27:
                
            filename = 'profile.json'
            with open(filename, 'r+') as profileData:
                                            
                data = json.load(profileData)
                data["Profiles"].append({'profileName': profileName, 'posList':[posList]})
                profileData.seek(0)
                json.dump(data, profileData)
                return False
        else:
            continue
        
        

    


def getProfile():
    filename = 'profile.json'
    with open(filename, 'r') as profileData:
        data = json.load(profileData)
        print('Profile Names')
        for i in data['Profiles']:
            print('---------------')
            print(i['profileName'])
            print('---------------')
        print('\n Enter Profile')
        print(' ---------------')
        profileInput = raw_input(' >')
        print('\n Enter number of times to run the profile pattern.')
        print(' ---------------')
        numberOfLaps = int(raw_input(' >'))

        print('\n Enter number of seconds for the pause.')
        print(' ---------------')
        numberOfSeconds = int(raw_input(' >'))

        increment = 0
        while(increment < numberOfLaps):
            engageProfile(profileInput)
            increment = increment + 1
            time.sleep(numberOfSeconds)
            
def engageProfile(profileName):
    filename = 'profile.json'
    with open(filename) as profileData:
        data = json.load(profileData)
        increment = 0
        for i in data['Profiles']:
            if(i['profileName'] == profileName):
                posList = i['posList']
                posString = str(posList[0])
                posObj = ast.literal_eval(posString)
                posLen = len(posObj['Positions'])
                while(increment < posLen ):
                    
                

                    
               
                    xy = str(posObj['Positions'][increment])
                    xy = xy.translate(None, 'u')
                    #d = json.loads(xy)
                    xyObj = ast.literal_eval(xy)
                    print(str(xyObj['xPos']) + ' ' + str(xyObj['yPos']))
                    x = int(xyObj['xPos'])
                    y = int(xyObj['yPos'])
                    pyautogui.click(x=x, y=y, clicks=posLen/2, button='left')
                    
                    increment = increment + 1
                    
                '''
                pyautogui.moveTo(xPos, yPos) 
                print('\n Input a number of desired clicks, leaving it empty will run for as long as the program is on')
                print(' ---------------')
                xClicks = raw_input(' >')
                if not (xClicks):
                    while('true'):
                        pyautogui.click() 
                
                else:
                    for i in range(int(xClicks)):
                        pyautogui.click() 
                        print(i)
                '''

def menu():
    print(' 1.Select Profile')
    print(' 2.New Profile')
    print(' 3.Exit')
    menuChoice = raw_input(' >')

    if(menuChoice == '1'):
        print('\n \n')
        getProfile()
        print('\n \n')
    if(menuChoice == '2'):
        storeProfile()

def start():
    
    
    while('true'):
        menu()
        

start()