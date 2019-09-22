#sudo pip3 install adafruit-circuitpython-servokit
import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def turnLeft():
    print("Left")
    kit.servo[0].angle = 89
    time.sleep(1)
    kit.servo[0].angle = 122

def turnRight():    
    print("Right")
    kit.servo[0].angle = 153
    time.sleep(1)
    kit.servo[0].angle = 122