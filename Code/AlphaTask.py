import Motors
import Servo 

#Go Forward for 4 seconds then turn right and keep going
#then stop
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


