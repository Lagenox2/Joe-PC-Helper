from tkinter import *
import os
import sys
import win32api
import win32con
import datetime
import time
import pyttsx3
import keyboard
from threading import Thread


engine = pyttsx3.init()
engine.setProperty('rate', 193)

def cmd_listen():
    return input()

def cmd_answer(comd):
    if comd == 'shutdown':
        engine.say('Just close the command prompt window by click and wait.')
        engine.runAndWait()
    else:
        print(f'Bad name of command {comd}.')

def command():
    os.system('cls')
    print()
    print('Operating System 1999-2024. All right reserved.')
    while True:
        cmd_answer(cmd_listen())