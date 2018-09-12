import curses
import Adafruit_BBIO.GPIO as GPIO
import time

#Set up curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

#Name button pins
buttonP="P9_20"
buttonM="P9_21"
buttonB="P9_22"
buttonR="P9_23"

# Set the GPIO pins:
GPIO.setup(buttonP, GPIO.IN)
GPIO.setup(buttonM, GPIO.IN)
GPIO.setup(buttonB, GPIO.IN)
GPIO.setup(buttonR, GPIO.IN)  

#create the window for the Etch-a-Sketch
begin_x = 0; begin_y = 0
height = 10; width = 11
win = curses.newwin(height, width, begin_y, begin_x)

#Set up boundry numbers
x=1
y=0
for x in range(1, 10):
    win.addstr(y,x,str(x))
    x = x+1
x=0
y=1
for y in range(1, 10):
    win.addstr(y,x,str(y))
    y = y+1

#Functions for each direction
def updateLEDR(channel):
    coor = win.getyx() #Get current position
    y,x = coor

    if(x == width-2): #check for edge and mark 'X'
            win.addstr(y,x,'X')
            win.move(y,x)
    else:
            win.addstr(y,x,'X')
    win.refresh() #Refreah window to show 'X'

def updateLEDL(channel):
    coor = win.getyx()
    y,x = coor

    if(x == 1):
            win.addstr(y,x,'X')
            win.move(y,x)
    else:
            win.addstr(y,x,'X')
            win.move(y,x-1)
    win.refresh()

def updateLEDU(channel):
    coor = win.getyx()
    y,x = coor

    if(y == 1):
            win.addstr(y,x,'X')
            win.move(y,x)
    else:
            win.addstr(y,x,'X')
            win.move(y-1,x)
    win.refresh()

def updateLEDD(channel):
    coor = win.getyx()
    y,x = coor

    if(y == height-1):
            win.addstr(y,x,'X')
            win.move(y,x)
    else:
            win.addstr(y,x,'X')
            win.move(y+1,x)
    win.refresh()

#GPIO listeners to detect button press and call correct method
GPIO.add_event_detect(buttonP, GPIO.FALLING, callback=updateLEDL)
GPIO.add_event_detect(buttonM, GPIO.FALLING, callback=updateLEDR)
GPIO.add_event_detect(buttonB, GPIO.FALLING, callback=updateLEDU)
GPIO.add_event_detect(buttonR, GPIO.FALLING, callback=updateLEDD)

#Loop to stay in code
try:
    
    while True:
        time.sleep(100)

#Manage interrupts and end curses program
except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()