from urllib.request import urlretrieve

# http://theremin.music.uiowa.edu/sound%20files/MIS/Piano_Other/piano/Piano.mf.G3.aiff
noteText = "C Db D Eb E F Gb G Ab A Bb B".split(" ")
for i in range(9,9+12*7+1):
    note = noteText[i%12] + str(i//12)
    print(note)
    urlretrieve("http://theremin.music.uiowa.edu/sound%20files/MIS/Piano_Other/piano/Piano.ff."+str(note)+".aiff","Notes/"+note+".aiff")