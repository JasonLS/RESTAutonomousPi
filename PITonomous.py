import os   
import time

os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #needed delay to setup
import pigpio #GPIO library

LeftMotor=4 #pin 7
RightMotor=14 #pin8

pi = pigpio.pi();
pi.set_servo_pulsewidth(LeftMotor, 0)
pi.set_servo_pulsewidth(RightMotor, 0) 


def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(LeftMotor, 0)
    pi.set_servo_pulsewidth(RightMotor, 0)     
    pi.stop()
    
def backward():
    print("Backward")
    pi.set_servo_pulsewidth(RightMotor, 1700)     
    pi.set_servo_pulsewidth(LeftMotor, 1700)     

def forward():
    print("Forward")
    pi.set_servo_pulsewidth(RightMotor, 1300)     
    pi.set_servo_pulsewidth(LeftMotor, 1300)
    
def still():
    print("Still...")
    pi.set_servo_pulsewidth(RightMotor, 1500)     
    pi.set_servo_pulsewidth(LeftMotor, 1500)

still()
time.sleep(2)
forward()
time.sleep(2)
still()
time.sleep(2)
backward()
time.sleep(2)
still()
stop()