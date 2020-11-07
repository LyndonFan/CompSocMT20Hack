import tkinter as tk
import pygame as pg
import time

#middleC = 60
majorIndicator = [True, False, True, False, True, True, False, True, False, True, False, True]
majorText = "CDEFGAB"
minorText = ["C#/D♭","D#/E♭","F#/G♭","G#/A♭","A#/B♭"]
noteText = "C Db D Db E F Gb G Ab A Bb B".split(" ")

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
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    

root = tk.Tk()
root.geometry("1000x400")
app = Application(master=root)

def convToNote(note):
    return noteText[note%12]+str(note//12)

pg.mixer.init()
pg.init()
pg.mixer.set_num_channels(50)

def playNote(note):
    print(convToNote(note))
    pg.mixer.music.load("Notes/{}.wav".format(convToNote(note)))
    pg.mixer.music.play()
    pg.mixer.music.unload()
    # wave_obj = sa.WaveObject.from_wave_file("Notes/{}.wav".format(convToNote(note)))
    # play_obj = wave_obj.play()
    # time.sleep(1)
    # play_obj.stop()

notes = {}
majorNotes = [36,38,40,41,43,45,47,48,50,52,53,55,57,59,60,62,64]
for i in range(len(majorNotes)):
    n = majorNotes[i]
    # print(n,majorText[i%7])
    b = tk.Button(text=majorText[i%7],height=10,width=5,bg="white",anchor="s",command=lambda: playNote(majorNotes[i]))
    b.place(x=50+50*i,y=50)
    notes[n] = b
    del b
extra = 0
minorNotes = [37,39,42,44,46,49,51,54,56,58,61,63]
for i in range(len(minorNotes)):
    n = minorNotes[i]
    # print(n,minorText[i%5])
    b = tk.Button(text=minorText[i%5],height=5,width=5,bg="white",command=lambda: playNote(n))
    extra += isMajor(n-2)
    # print(extra)
    b.place(x=25+50*(i+extra),y=50)
    notes[n] = b
    del b
playNote(36)
app.mainloop()