import Motors
import Servo 

#Autonomous Movement: Ideal: Vehicle starts after a time delay of about 5 seconds,
#moves 3 meters forward, turns right, moves forward 3 meters and stops. Minimum Task
#for partial points: Vehicle Starts and moves forward.
#Additional partial points for moving forward combined with turning or stopping.

time.sleep(5) #Wait 5 seconds


Motors.forward()
time.sleep(2)
Servo.turn_right()
time.sleep(2)
Servo.center()
Motors.still()
Servo.cleanup()
Motors.stop()


