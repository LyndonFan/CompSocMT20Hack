import tkinter as tk
from tkinter import ttk
import pygame as pg
import time

#middleC = 60
majorIndicator = [True, False, True, False, True, True, False, True, False, True, False, True]
majorText = "CDEFGAB"
minorText = ["C#/D♭","D#/E♭","F#/G♭","G#/A♭","A#/B♭"]
noteText = "C Db D Eb E F Gb G Ab A Bb B".split(" ")

def isMajor(x):
    return majorIndicator[((x%12)+12)%12]

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.notes = []
        self.create_widgets()

    def create_widgets(self):
        pass
        # self.hi_there = ttk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = ttk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")
    

root = tk.Tk()
root.geometry("1000x300")
app = Application(master=root)

def convToNote(note):
    res = noteText[note%12]+str(note//12)
    print(res)
    return res

pg.mixer.init()
pg.init()
pg.mixer.set_num_channels(50)

channels = [pg.mixer.Channel(i) for i in range(65-36)]
sounds = [pg.mixer.Sound("Notes/{}.wav".format(convToNote(note))) for note in range(36,65)]

def playNote(note):
    print(convToNote(note))
    channels[note-36].play(sounds[note-36],maxtime=2000)
    # wave_obj = sa.WaveObject.from_wave_file("Notes/{}.wav".format(convToNote(note)))
    # play_obj = wave_obj.play()
    # time.sleep(1)
    # play_obj.stop()

for c in channels:
    c.set_volume(0)
keyBinds = list("cfvgbnjmk,l.q2w3er5t6y7ui9o0p")

notes = {}
majorNotes = [36,38,40,41,43,45,47,48,50,52,53,55,57,59,60,62,64]
for i in range(len(majorNotes)):
    n = majorNotes[i]
    # print(n,majorText[i%7])
    b = tk.Button(
        text=majorText[i%7],height=10,width=5,
        highlightbackground="white",fg="black",
        anchor="s",command=lambda z=n: playNote(z)
    )
    b.bind(keyBinds[n-36],lambda z=n: playNote(z))
    b.place(x=50+50*i,y=50)
    notes[n] = b
extra = 0
minorNotes = [37,39,42,44,46,49,51,54,56,58,61,63]
for i in range(len(minorNotes)):
    n = minorNotes[i]
    # print(n,minorText[i%5])
    b = tk.Button(
        text=minorText[i%5],height=5,width=5,
        highlightbackground="black",fg="white",
        command=lambda z=n: playNote(z)
    )
    b.bind(keyBinds[n-36],lambda z=n: playNote(z))
    extra += isMajor(n-2)
    # print(extra)
    b.place(x=25+50*(i+extra),y=50)
    notes[n] = b

for i in range(len(keyBinds)):
    root.bind(keyBinds[i],lambda inp,z=36+i: playNote(z))
root.bind("/",lambda inp,z=48: playNote(z))

for c in channels:
    c.set_volume(1)
app.mainloop()