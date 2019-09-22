import Motors
import Servo
import os
import time

#Autonomous Movement: Ideal: Vehicle starts after a time delay of about 5 seconds,
#moves 3 meters forward, turns right, moves forward 3 meters and stops. Minimum Task
#for partial points: Vehicle Starts and moves forward.
#Additional partial points for moving forward combined with turning or stopping.
os.system("flite -t 'Alpha Task started'")
Motors.still()
time.sleep(5) #Wait 5 seconds


Motors.forward()
time.sleep(2)
Servo.turnRight()
time.sleep(2)
Servo.turnStraight()
Motors.still()
Servo.cleanup()
Motors.stop()
os.system("flite -t 'Alpha Task ended'")



