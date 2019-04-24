import Ultrasonic
import time
import Motors
import Servo

SerialPort1 = '/dev/ttyUSB0'

FrontSensor = Ultrasonic.MySensor(SerialPort1)
FrontSensor.start()

while FrontSensor.getLastEvent() >= 1000: #3000 millimeters
    print(FrontSensor.getLastEvent())
    Motors.forward()
    if FrontSensor.getLastEvent() <= 1000:
        Servo.turn_right()
        time.sleep(.5)
        Servo.turn_left()
        time.sleep(.5)
        Motors.still()
        Servo.cleanup()
        Motors.stop()
        FrontSensor.stop()
        break
    
        
        
#call .stop() to stop reading

