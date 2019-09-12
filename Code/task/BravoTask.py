import Motors
import Servo
import Ultrasonic
import time
import os

#Autonomous Obstacle Sensitivity Vehicle should move forward until it senses an
#obstacle (such as a team member, or judge) and stops. The obstacle will move into the
#path after movement begins at a distance between 3-10 meters. If no obstacle is
#sensed the vehicle should run at least 10 meters. Vehicle must complete three course
#runs for full points.

SerialPort1 = '/dev/ttyUSB0'

FrontSensor = Ultrasonic.MySensor(SerialPort1)
FrontSensor.start()
os.system("flite -t 'Bravo Task started'")

while FrontSensor.getLastEvent() >= 3000: #3000 millimeters
    print(FrontSensor.getLastEvent())
    Motors.forward()
    if FrontSensor.getLastEvent() <= 3000:
        Motors.still()
        os.system("flite -t 'Bravo Task ended'")

    #Avoid and keep going
    #if FrontSensor.getLastEvent() <= 3000:
    #    Servo.turn_right()
    #    time.sleep(.5)
    #    Servo.turn_left()
    #    time.sleep(.5)
    #    Motors.still()
    #    Servo.cleanup()
    #    Motors.stop()
    #    FrontSensor.stop()
    #    break
    
        
        
#call .stop() to stop reading

