import os #launches pigpiod library which lets us communicate with motors
import time #allows us to set delays
import pigpio #imports GPIO library

os.system("sudo pigpiod") #Launching GPIO library

time.sleep(1) #needed delay to setup

Motor_Pin = 4 #sets motor pin to pin 4 on BCM, physical pin 5

Motors = pigpio.pi(); #SHortcut naming
pi.set_servo_pulsewidth(Motor_Pin, 0) #Sets a neutral pulse to motors telling it to get ready for communication
    
def forward():
    print("Forward")
    Motors.set_servo_pulsewidth(Motor_Pin, 1350)
    
def backward():	 
    print("Backward")
    Motors.set_servo_pulsewidth(Motor_Pin, 1650)
    
def forwardFast():
    print("Forward")
    Motors.set_servo_pulsewidth(Motor_Pin, 1100) 
    
def backwardFast():	 
    print("Backward")
    Motors.set_servo_pulsewidth(Motor_Pin, 1900) 
    
def still(): 
    print("Still...")
    Motors.set_servo_pulsewidth(Motor_Pin, 1500)
    
def stop(): #This will stop communication and cleanup. Use "Still()" to stop motors if you plan to keep using them
    print("Stoping Motors and Initiating Cleanup...")
    Motors.set_servo_pulsewidth(Motor_Pin, 0)
    Motors.stop()
