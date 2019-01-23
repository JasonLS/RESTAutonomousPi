From Motors import *
From Servo import *

os.system ("sudo pigpiod") #Launching GPIO library needed for motors
time.sleep(1) #needed delay to setup


forward()
time.sleep(2)
turn_left()
time.sleep(2)
stop_turning()
still()
time.sleep(2)
turn_right()
time.sleep(2)
stop_turning()
still()
stop()
