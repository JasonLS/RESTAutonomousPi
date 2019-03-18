 	import os   
import time

os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #needed delay to setup
import pigpio #GPIO library
import RPi.GPIO as GPIO
import Servo
GPIO.setmode(GPIO.BCM)
FPin=19
DPin=16
LPin=26
RPin=20
GPIO.setup(FPin, GPIO.IN)#up
GPIO.setup(BPin, GPIO.IN)#down
GPIO.setup(LPin, GPIO.IN)#left 
GPIO.setup(RPin, GPIO.IN)#right

Forwardinput_value = GPIO.input(FPin)
Backwardinput_value = GPIO.input(BPin)
Leftinput_value = GPIO.input(LPin)
Rightinput_value = GPIO.input(RPin)


Motors=4

pi = pigpio.pi();
pi.set_servo_pulsewidth(Motors, 0)


def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    print("Stopping")
    pi.set_servo_pulsewidth(Motors, 0)
    pi.stop()
    
def backward():
    print("Backward")
    pi.set_servo_pulsewidth(Motors, 1600)     

def forward():
    print("Forward")
    pi.set_servo_pulsewidth(Motors, 1400)
    
def still():
    print("Still...")
    pi.set_servo_pulsewidth(Motors, 1500)

if Forwardinput_value == 1:
    print("Forward")

elif Backwardinput_value == 1:
    print("Backward")

elif Leftinput_value == 1:
    print("Left")

elif Rightinput_value == 1:
    print("Right")


