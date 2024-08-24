from tkinter import *
import os
import sys
import win32api
import win32con
import datetime
import time
import pyttsx3
from win32api import GetComputerName, SendMessage
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
        em = open('email.info', 'w')
        em.truncate(0)
        em.write("if you reading this, it means that you now that you can stop this BIGGEST mistake."
                 "You will delete Joe's part that is virus on your PC. His addons are parts of big virus. If you will not stop him, it's will be too late. good luck.")
        em.close()
        os.system('run.vbs')
        time.sleep(0.2)
        keyboard.send('alt+TAB')
        time.sleep(0.2)
        keyboard.send('alt+F4')
    elif comd == 'help':
        print('shutdown\n start diskexp\n start browser\n email')
    elif comd == 'start diskexp':
        os.system('start explorer')
    elif comd == 'start browser':
        os.system('start https://google.com')
    elif comd == 'email':
        em = open('email.info', 'r')
        print(em.readlines())
    else:
        print(f'Bad name of command {comd}.')

def command():
    os.system('cls')
    print()
    print(f'Operating System 1999-2024. All right reserved. {pc_name}://{os.getlogin()}')
    while True:
        cmd_answer(cmd_listen())