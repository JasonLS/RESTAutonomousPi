#sudo pip3 install adafruit-circuitpython-servokit
import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


    
def forward():
    kit.servo[1].angle = 100
    time.sleep(.5)
    print("Forward")
    kit.servo[1].angle = 80
    
def backward():  
    kit.servo[1].angle = 100
    time.sleep(.5)
    print("Backward")
    kit.servo[1].angle = 110
    
def forwardFast():
    kit.servo[1].angle = 100
    print("Forward but faster")
    kit.servo[1].angle = 70
    
def backwardFast():  
    kit.servo[1].angle = 100
    print("Backward but faster")
    kit.servo[1].angle =  120
    
def still(): 
    print("Still...")
    kit.servo[1].angle = 100
    
def stop(): #This will stop communication and cleanup. Use "Still()" to stop motors if you plan to keep using them
    print("Stoping Motors and Initiating Cleanup...")
    kit.servo[1].angle = 0
    
    
    
def forwardTime(value):
    value = int(value)
    kit.servo[1].angle = 100
    time.sleep(.5)
    print("Forward")
    kit.servo[1].angle = 80
    time.sleep(value)
    kit.servo[1].angle = 100
    
def backwardTime(value):
    value = int(value)
    kit.servo[1].angle = 100
    time.sleep(.5)
    print("Backward")
    kit.servo[1].angle = 110
    time.sleep(value)
    kit.servo[1].angle = 100
    
    