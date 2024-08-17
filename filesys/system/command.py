from tkinter import *
import os
import win32api
import win32con
import datetime
import time
import keyboard
from threading import Thread



def cmd_listen():
    return input()

def cmd_answer(comd):
    file = open('commands.conf', 'r')
    ALL_COMMANDS = file.readlines()
    ALL_COMMANDS[0] = ALL_COMMANDS[0][3:-3]
    if comd in ALL_COMMANDS:
        if comd == 'shutdown':
            os.system('exit')
    else:
        print(f'Bad name of command {comd}.')

def command():
    os.system('cd')
    while True:
        cmd_answer(cmd_listen())