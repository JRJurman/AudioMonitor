# AudioMonitor


AV Muter that is triggered by extended periods of loud input from the microphone
Created by Jesse R Jurman and Ethan H Jurman

This program is facilitated by 2 scripts:
    
- AVMuter.py  | A python script (2.x or 3.x) that generates the black screen, countdown, and image
    
- Trigger.ahk | A AutoHotKeys file that listens for audio, mutes applications, and kicks-off AVMuter.py

There are several other files and libraries:
    
- shhhh.gif   | A gif image that is loaded at the bottom of the AVMuter screen
    
- lib/VA.ahk  | Audio Libraries for Windows Vista and later

There are several dependencies and requirements for this application to work. If you have any questions, feel free to email me at jrjurman@gmail.com; Understand that this program is open-source and provided as is. I'm not responsible if your computer becomes an unusable pile of goo as a result of running this.

# To Run the Application



### Install Dependencies:


- Install AutoHotKeys (v1.1) [tested on v1.1.14.03]
  - http://www.autohotkey.com/
  - [in case the above link points to v1.0](http://ahkscript.org/download/1.1/)



- Install Python (2.7 or 3.3) [tested on 3.3.5rc1]
  - https://www.python.org/downloads/
  - Be sure when installing Python, you include the Tkinter library

 
### Open Sound Prefrences:
  _This might seem odd, but in order for AutoHotKeys to grab your microphone, the meter must be open_
  - Right Click sound icon in the bottom right > Recording Devices
  - Leave this window open


### Run Trigger.ahk
  - Download the AudioMonitor [you can download and then extract them from here](https://github.com/JRJurman/AudioMonitor/archive/master.zip )
  - Simply double click Trigger.ahk from the source directory!

# Configuring AudioMonitor

In the Trigger.ahk file, you'll find several variables which can be modified to your settings. I'll explain each variable here so that you have a better idea of what these variables do.

### tAudio
__Volume which triggers program (lowest = 0.00, highest = 1.00).__

This variable is important if your microphone is prone to picking up background noise (such as an air-conditioner or the speakers to the computer).
Values range from 0.00 (will pick up anything) to 1.00 (will only pick up audio that spikes the microphone).
Setting this anywhere from 0.10 to 0.90 are normal, check your microphone meter (from opening the sound prefrences) to see where it usually sits at.

### tLimit
__Number of periods where audio is over tAudio to trigger program (set as tCounter below).__

This variable is important if your microphone is prone to picking up random spikes of noise.
The values here correspond to a 'device period' which is small, so feel free to keep this in the hundreds range (think ms).
Setting this anywhere from 120 and up works... Smaller values may cause the program to trigger prematurely.

### tDLimit
__Periods of delay before we reset tCounter to 0.__

This variable is the number of 'device periods' before we reset the value that would reach our tLimit.
If the program picks up a lot of audio (but not quite enough to hit the tLimit), this value is how many device periods before we decide that we have to start over.
Setting this anywhere around 40 seems to work... Too small and you'll never hit the tLimit, too large and you might hit the tLimit from random noise over time.

### pDelay 
__Number of seconds that programs are muted and screen is blacked out.__

This variable is the number of seconds that the screen is blacked out and audio is muted. This is directly passed into AVMuter.py

### pPunish
__Number of seconds that are added to pDelay for everytime we have to black out.__

This variable can be 0 (to keep the delay unchanged) and positive to make consecutive delays longer.
i.e. a pDelay of 30 and pPunish of 5 will delay the following number of seconds: 30, 35, 40, 45, ... 
N.B. It's probably not wise to set this negative...

### fSize
__Size of Font on Blackout__
This is the size of the font on the countdown. 
I recognize that some displays will be larger / smaller than what I use, so this should alleviate any resolution issues.
