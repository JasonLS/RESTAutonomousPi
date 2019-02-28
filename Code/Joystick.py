import os   
import time

os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #needed delay to setup
import pigpio #GPIO library
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)#up
GPIO.setup(16, GPIO.IN)#down
GPIO.setup(26, GPIO.IN)#left 
GPIO.setup(20, GPIO.IN)#right



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


