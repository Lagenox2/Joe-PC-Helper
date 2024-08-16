from tkinter import *
import os
import win32api
import win32con
import datetime
import time
from threading import Thread


def command():
    command_win = Tk()
    command_win.title('© 2024 Operating System. All rights reserved. Command Prompt')
    command_win.resizable(False, False)
    command_win.geometry('980x514')
    canvas = Canvas(command_win, width=command_win.winfo_width(), height=command_win.winfo_height(), bg='black')
    canvas.pack()
    command_win.mainloop()
