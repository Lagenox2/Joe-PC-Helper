import time
import keyboard
from filesys.system.command import command
from threading import Thread
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 193)

def joe_work():
    file = open('base-addon.conf', 'r')
    if file.readline() == 'no':
        time.sleep(3)
        engine.say('By the way, I have and addon that helps me to better manage your Operating System. I will open it in browser and start loading it...')
        engine.runAndWait()
        time.sleep(2)
        engine.say('Please, confirm starting my addon wizard by pressing enter when focused on my window.')
        engine.runAndWait()
        keyboard.wait('enter')
        engine.say('While this addon installing on your disk, I will tell you how to use your operating system. If you want to shutdown the OS, type. s h u t d o w n. '
                   'shutdown in the command prompt window. If you want to explore your disk, enter in the cmd start diskexp. s t a r t space d i s k e x p. If you want to browse the internet,'
                   'enter in the cmd start browser. s t a r t space b r o w s e r.')
        engine.runAndWait()
        time.sleep(2)
        engine.say('My addon successfully installed.')
        engine.runAndWait()
        file.close()
        file = open('base-addon.conf', 'w')
        file.truncate(0)
        file.write('yes')
        file.close()
    else:
        pass

def boot():
    work = Thread(target=joe_work)
    work.start()
    command()
