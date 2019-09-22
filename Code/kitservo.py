#sudo pip3 install adafruit-circuitpython-servokit
import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)



#kit.servo[0].angle = 180
#time.sleep(1)
#kit.servo[0].angle = 0
#time.sleep(1)
#kit.servo[0].angle = 180
#time.sleep(1)
#kit.servo[0].angle = 122
print("it just works")



while 1:
    user_input = int(input("CHoose Speed:  \n"))
    
    if user_input > 0:
        kit.servo[0].angle = user_input
        time.sleep(1)
        kit.servo[0].angle = 122
        
    else:
        break
    

#80 forwards
#91-100 is dead zone
#110 backwards
#kit.servo[1].angle = 90  #80 f 180 FAstbasck
#time.sleep(1)
#kit.servo[1].angle = -40
#time.sleep(1)
#kit.servo[1].angle = 90
#time.sleep(1)
#kit.servo[1].angle = 110
#time.sleep(1)
#kit.servo[1].angle = 0
#time.sleep(1)

#kit.servo[0].angle = 122
#kit.servo[1].angle = 90
print("done")