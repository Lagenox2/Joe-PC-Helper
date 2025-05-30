import shutil
import subprocess
import time
import tkinter as tk
import os
import sys
from tkinter import messagebox as mb
import winsound

from PIL import Image
from PIL import ImageTk

from tkinter import *
from time import *
import win32api
from win32api import ShowCursor
import win32con
import pyttsx3
import keyboard
import time
from threading import Thread
from pyqadmin import admin
from random  import randint
import codecs
from filesys.system.system import *

engine = pyttsx3.init()
engine.setProperty('rate', 193)

ShowCursor(-1)

global mng


def clnd():
    calendwin = Tk()
    calendwin.title("Joe's calendar")
    calendwin.geometry('500x300')
    text = 'CALENDAR'
    lbl = Label(calendwin, text=text)
    calendwin.resizable(False, False)
    process = Thread(target=menu(lbl, calendwin))
    process.start()
    calendwin.mainloop()

def clnd_int(win: Tk, lbl: Label):
    lbl.pack()
    engine.say('What do you want to add in your calendar?')
    engine.runAndWait()
    inp = input()
    lbl.destroy()
    lbl = Label(win, text=inp)
    lbl.pack()
    engine.say('I will keep your plan in mind.')
    engine.runAndWait()
    menu(lbl, win)

class Action:
    def __init__(self):
        pass

    def leftMouseClick(self, x1, y1, x2, y2):
        try:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, x2, y2)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1, y1, x2, y2)
        except:
            pass

    def rightMouseClick(self, x1, y1, x2, y2):
        try:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x1, y1, x2, y2)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x1, y1, x2, y2)
        except:
            pass

    def mousePos(self, x, y):
        win32api.SetCursorPos((x, y))

    def printLine(self, line):
        for i in line:
            print(i, end='')
            time.sleep(0.05)
        print()

def browsing():
    os.system('start http://')

def os_start():
    engine.say('Welcome. To your Operating System.')
    engine.runAndWait()
    boot()

def oper_sys():
    os_start()

def playing():
    engine.say('Please wait...')
    engine.runAndWait()
    sleep(1)
    os.system('compile.bat')
    sleep(2)
    oper_sys()

def infact():
    engine.setProperty('rate', 180)
    fileObj = codecs.open("facts.txt", "r", "utf_8_sig")
    text = fileObj.read()
    facts = text.split('\n')
    engine.say(facts[randint(0, len(facts))])
    engine.runAndWait()
    fileObj.close()
    engine.setProperty('rate', 193)

def joke():
    with open('jokes.txt', 'r') as file:
        jokes = [line for line in file]
    engine.say(jokes[randint(0, len(jokes))])
    engine.runAndWait()

def manage(text, win):
    mng = Tk('Manage')
    mng.title('Manage')
    mng.resizable(False, False)
    mng.geometry('100x300')
    browse = Button(mng, text='Browse', bg='grey', fg='white', height=5, width=20)
    browse.pack()
    browse.config(command=browsing)
    play = Button(mng, text='Your OS', bg='grey', fg='white', height=5, width=20)
    play.pack()
    play.config(command=playing)
    intfact = Button(mng, text='Interesting fact', bg='grey', fg='white', height=5, width=20)
    intfact.pack()
    intfact.config(command=infact)
    jok = Button(mng, text='Joke', bg='grey', fg='white', height=5, width=20)
    jok.pack()
    jok.config(command=joke)
    mng.mainloop()
    menu(text, win)

def menu(text, win):
    engine.say('If you want me to help you to manage your system, enter "manage" in command prompt window. '
               'If you want me to interact with calendar and write there some data, type clnd_int')
    engine.runAndWait()
    print('If you want me to help you to manage your system, enter "manage" in command prompt window.'
               'If you want me to interact with calendar and write there some data, type clnd_int')
    choice = input()
    if choice == 'manage':
        engine.say('Ok, proceed.')
        engine.runAndWait()
        manage(text, win)
    elif choice == 'clnd_int':
        pracess = Thread(target=clnd)
        pracess.start()
        clnd_int(win, text)
    else:
        menu(text, win)

def start():
    name = open('name.dll', 'r')
    username = name.read()
    name.close()
    if username == '':
        name = open('name.dll', 'w')
        engine.say('Hi, my name is Joe. Im your virtual assistant.')
        engine.runAndWait()
        engine.say('What is your name? Type your name in the command prompt window.')
        engine.runAndWait()
        actions.printLine('What is your name?')
        usrnm = input()
        name.write(usrnm)
        engine.say('Beautiful name.')
        engine.runAndWait()
        clnd()
    else:
        engine.say(f'Welcome back, {username}.')
        engine.runAndWait()
        clnd()

def start2():
    menu()

def stay():
    pass

def checkstate():
    file = open('system.state', 'r')
    while file.read() != 'shutdowned':
        pass
    sys.exit()

filename = 'Joe.bat'
dir_name = f'C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
shutil.copy(filename, dir_name)

actions = Action()
root = tk.Tk()

root.wait_visibility(root)
root.wm_attributes("-fullscreen", 1)
root.wm_attributes("-transparentcolor", root['bg'])

root.title('joe.bat')

frame = tk.Frame(root)
frame.grid()

root.iconphoto(False, tk.PhotoImage(file='joe.png'))

canvas = tk.Canvas(frame, width=root.winfo_width(), height=root.winfo_height())
img = ImageTk.PhotoImage(file='joe1.png')
image = canvas.create_image(0, 0, anchor='nw', image=img)
canvas.coords(image, 500, 150)
'''img2 = tk.PhotoImage(file='hand.png')
image2 = canvas.create_image(0, 0, anchor='nw', image=img2)
canvas.coords(image2, 100, 100)'''
canvas.pack()

process1 = Thread(target=start)
process1.start()
check = Thread(target=checkstate)
check.start()

root.mainloop()
