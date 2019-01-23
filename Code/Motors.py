import os   
import time

#os.system ("sudo pigpiod") #Launching GPIO library
#time.sleep(1) #needed delay to setup
import pigpio #GPIO library
Motors=4

pi = pigpio.pi();
pi.set_servo_pulsewidth(Motors, 0)


def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    print("Stopping")
    pi.set_servo_pulsewidth(Motors, 0)
    pi.stop()
    
def backward():
    print("Backward")
    pi.set_servo_pulsewidth(Motors, 1700)     

def forward():
    print("Forward")
    pi.set_servo_pulsewidth(Motors, 1300)
    
def still():
    print("Still...")
    pi.set_servo_pulsewidth(Motors, 1500)

##still()
##time.sleep(2)
##forward()
##time.sleep(2)
##still()
##time.sleep(2)
##backward()
##time.sleep(2)
##still()
##stop()
