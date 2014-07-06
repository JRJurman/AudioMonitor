import sys, time, os.path
from subprocess import call
if sys.version_info[0]==2: #Just checking your Python version to import Tkinter properly.
    from Tkinter import *;
else:
    from tkinter import *;
	
master = Tk()

# Volume which triggers program (lowest = 0.01, highest = 1.00)
tAudio = Scale(master, label="Volume which triggers program (lowest = 0.01, highest = 1.00, default = 0.01)", length=500, from_=0.01, to=1.00, resolution=0.01, orient=HORIZONTAL)
tAudio.set(0.1)
tAudio.pack()
# Number of periods where audio is over tAudio to trigger program (set as tCounter below)
tLimit = Scale(master, label="Number of periods where audio is over tAudio to trigger program (default = 120)", length=500, from_=0, to=500, orient=HORIZONTAL)
tLimit.set(120)
tLimit.pack()
# Periods of delay before we reset tCounter to 0
tDLimit = Scale(master, label="Periods of delay before we reset tCounter to 0 (default = 40)", length=500, from_=0, to=60, orient=HORIZONTAL)
tDLimit.set(40)
tDLimit.pack()
# Number of seconds that programs are muted and screen is blacked out
pDelay = Scale(master, label="Number of seconds that programs are muted and screen is blacked out (default = 5)", length=500, from_=0, to=60, orient=HORIZONTAL)
pDelay.set(5)
pDelay.pack()
# Number of seconds that are added to pDelay for everytime we have to black out
pPunish = Scale(master, label="Seconds that are added to the delay for everytime we have to black out (default = 5)", length=500, from_=0, to=60, orient=HORIZONTAL)
pPunish.set(5)
pPunish.pack()
# Size of Font on Blackout
fSize = Scale(master, label="Size of Font on Blackout (default = 80)", length=500, from_=8, to=120, orient=HORIZONTAL)
fSize.set(80)
fSize.pack()

def executeProgram():
	if(os.path.isfile("Trigger.exe")):
		call(["Trigger.exe", str(tAudio.get()), str(tLimit.get()), str(tDLimit.get()), str(pDelay.get()), str(pPunish.get()), str(fSize.get())])
	else:
		call(["AutoHotKey.exe", "Trigger.ahk", str(tAudio.get()), str(tLimit.get()), str(tDLimit.get()), str(pDelay.get()), str(pPunish.get()), str(fSize.get())])
	exit()
	
b = Button(master, text="Run", command=executeProgram)
b.pack(side="right", padx = 15, pady = 10)

def close():
	exit()
	
b = Button(master, text="Close", command=close)
b.pack(side="right", padx = 15, pady = 10)

mainloop()