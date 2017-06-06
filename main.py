import gui
from tkinter import *
import commands
from Database import data
import threading
from VoiceRec import voiceRec
from multiprocessing import Process


def main():
    root = Tk()
    screen = gui.gui(root)

    root.geometry("700x600")
    commands.Commands(screen)
    voice=voiceRec(screen)
    data("goodreads_library_export.csv")
    root.resizable(width=False, height=False)
    p=Process(target=voice.main)
    p.start()
    p2=Process(target=root.mainloop)
    p2.start()
    threading.Thread(target=voice.main()).start()
    threading.Thread(target=root.mainloop()).start()


if __name__ == "__main__":
    main()
