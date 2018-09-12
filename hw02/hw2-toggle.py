import Adafruit_BBIO.GPIO as GPIO
import time

#Set gpio pin for LED
GPIO.setup("P9_27", GPIO.OUT)

# Loop alternating pin, flashing LED
while True:
    GPIO.output("P9_27", GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output("P9_27", GPIO.LOW)
    time.sleep(0.0005)