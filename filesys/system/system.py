from filesys.system.command import command
import winsound


def boot():
    filename = 'welcome.mp3'
    winsound.PlaySound(filename, winsound.SND_FILENAME)
    command()
