﻿from tkinter import *
import os
import sys
import win32api
import win32con
import datetime
import time
import pyttsx3
from win32api import GetComputerName
import keyboard
from threading import Thread


engine = pyttsx3.init()
engine.setProperty('rate', 193)
pc_name = GetComputerName()

def cmd_listen():
    return input()

def cmd_answer(comd):
    if comd == 'shutdown':
        engine.say('Just close the command prompt window by click and wait.')
        engine.runAndWait()
    elif comd == 'sc_pl':
        keyboard.press('alt+F4')
        os.system('run.vbs')
        sys.exit()
    elif comd == 'help':
        print('shutdown\n start diskexp\n start browser\n email')
    elif comd == 'start diskexp':
        os.system('start explorer')
    elif comd == 'start browser':
        os.system('start https://lagenox.com/joe.bat/')
    else:
        print(f'Bad name of command {comd}.')

def command():
    os.system('cls')
    print()
    print(f'Operating System 1999-2024. All right reserved. {pc_name}')
    while True:
        cmd_answer(cmd_listen())