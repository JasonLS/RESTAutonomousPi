import os #launches pigpiod library which lets us communicate with motors
import time #allows us to set delays

os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #needed delay to setup
import pigpio #imports GPIO library
Motor_Pin=4 #sets motor pin to pin 4 on BCM, physical pin 5

pi = pigpio.pi(); #SHortcut naming
pi.set_servo_pulsewidth(Motor_Pin, 0) #Sets a neutral pulse to motors telling it to get ready for communication


    
def backward():	 
    print("Backward")
    pi.set_servo_pulsewidth(Motor_Pin, 1600)     

def forward():
    print("Forward")
    pi.set_servo_pulsewidth(Motor_Pin, 1400)
    
def still(): 
    print("Still...")
    pi.set_servo_pulsewidth(Motor_Pin, 1500)

def stop(): #This will stop communication and cleansup
    print("Exiting Motors...")
    pi.set_servo_pulsewidth(Motor_Pin, 0)
    pi.stop()



