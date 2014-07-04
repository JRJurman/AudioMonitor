import sys, time
if sys.version_info[0]==2: #Just checking your Python version to import Tkinter properly.
    from Tkinter import *;
else:
    from tkinter import *;

top=Tk();
top.configure(background='black')

# Binding to close using escape
#top.bind("<Escape>", lambda x: exit())

# Buffer
Label( top, text=" ", bg="black", fg="navajo white", font=(None, 40) ).pack()

# Use the argument value as font size
# Otherwise, set it to 80
if (len(sys.argv) > 2):
    s = int(sys.argv[2])
else:
    s = 80

var = StringVar()
label = Label( top, textvariable=var, bg="black", fg="navajo white", font=(None, s) )

# Use the argument value as the countdown start
# Otherwise, set to 60
if (len(sys.argv) > 1):
    var.set(sys.argv[1])
else:
    var.set(str(60))
label.pack()

top.attributes("-fullscreen", True)

render = PhotoImage(file="shhhh.gif")
renderLabel = Label( top, image=render );
renderLabel.pack( side=BOTTOM )
def countdown():
    var.set(str(int(var.get())-1))
    if (int(var.get()) > 0): 
        top.after(1000, countdown)
    else:
        exit()

if __name__ == '__main__':
    countdown()
    top.mainloop();
