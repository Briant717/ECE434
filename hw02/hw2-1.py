#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

# Set buttons and LEDs to pins
buttonP="P9_20"
buttonM="P9_21"
buttonB="P9_22"
buttonR="P9_23"

LEDp="P9_24"
LEDm="P9_25"
LEDb="P9_26"
LEDr="P9_27"

# Set the GPIO pins:
GPIO.setup(LEDp,GPIO.OUT)
GPIO.setup(LEDm,GPIO.OUT)
GPIO.setup(LEDb,GPIO.OUT)
GPIO.setup(LEDr,GPIO.OUT)
GPIO.setup(buttonP, GPIO.IN)
GPIO.setup(buttonM, GPIO.IN)
GPIO.setup(buttonB, GPIO.IN)
GPIO.setup(buttonR, GPIO.IN)  

# Map buttons to LEDs
map = {buttonP: LEDp, buttonM: LEDm, buttonB: LEDb, buttonR: LEDr}

def updateLED(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print(map[channel] + " Toggled")

print("Running...")
# Add events to detect button presses
GPIO.add_event_detect(buttonP, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(buttonM, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(buttonB, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(buttonR, GPIO.BOTH, callback=updateLED)

# Loop to stay in code
try:
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()