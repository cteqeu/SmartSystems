from subprocess import Popen, PIPE, STDOUT
import tkinter as tk
from tkinter import Tk
from threading import Thread


def create_worker(target):
    return Thread(target=target)


def start_worker(worker):
    worker.start()


def commande():
    cmd = 'ping www.cteq.eu'
    p = Popen(cmd.split(), stdout=PIPE, stderr=STDOUT)
    for line in iter(p.stdout.readline, ''):
        nom_mp4 = tk.Label(root, text=line)
        nom_mp4.pack()

root = Tk()
root.geometry('300x190+400+400')

worker = create_worker(commande)
tk.Button(root, text='Ping', command=lambda: start_worker(worker)).pack()

root.mainloop()