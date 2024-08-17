from tkinter import *
import os
import win32api
import win32con
import datetime
import time
import keyboard
from threading import Thread


def command():
    os.system('start cmd.exe')
    keyboard.write('@echo off')
    keyboard.send('enter')
    keyboard.write('cls')
    keyboard.send('enter')
    keyboard.write('echo on')
    keyboard.send('enter')
