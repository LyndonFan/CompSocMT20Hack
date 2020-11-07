import tkinter as tk

#middleC = 60
majorIndicator = [True, False, True, False, True, True, False, True, False, True, False, True]
majorText = "CDEFGAB"

def isMajor(x):
    return majorIndicator[((x%12)+12)%12]

class GenNote:
    def __init__(self, startingNote):
        self.note = startingNote
        self.isMajor = isMajor(self.note)
    
    def nextNote(self):
        incre = 1
        while not(isMajor(self.note)==isMajor(self.note+incre)):
            incre += 1
        self.note += incre
        return self.note


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
root.geometry("600x1200")
app = Application(master=root)
major = GenNote(60-12-1)
notes = {}
for i in range(17):
    n = major.nextNote()
    b = tk.Button(text=majorText[i%7],height=10,width=5,bg="#FFFFFF").place(x=50+50*i,y=50)
    notes[n] = b
minor = GenNote(60-1)
app.mainloop()