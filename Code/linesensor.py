import RPi.GPIO as GPIO
from Motors import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN) #Right
GPIO.setup(26, GPIO.IN) #Left
GPIO.setwarnings(False)
still()
while 1:
    forward()
    if GPIO.input(26) == 1:
        print("Detected")
        still()
    elif GPIO.input(20) == 1:
        print("Detected")
        still()
