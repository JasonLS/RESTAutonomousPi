from PITonomous import *
from Servo import *
GPIO.setwarnings(False)

forward()
time.sleep(3)
turn_left()
time.sleep(2)
stop_turning()
still()
backward()
time.sleep(2)
turn_right()
time.sleep(3)
stop_turning()
still()
stop()
