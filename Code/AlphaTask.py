import Motors
import Servo 

#Stop and GO
Motors.forward()
time.sleep(2)
Servo.turn_left()
time.sleep(2)
Servo.stop_turning()
Motors.still()
time.sleep(2)
Servo.turn_right()
time.sleep(2)
Servo.stop_turning()
Motors.still()
Servo.cleanup()
Motors.stop()


#Continous