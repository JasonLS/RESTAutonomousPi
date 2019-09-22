import KitMotor
import KitSteer
import Ultrasonic
import time

from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)


SerialPort1 = '/dev/ttyUSB1'

FrontSensor = Ultrasonic.MySensor(SerialPort1)
FrontSensor.start()
KitMotor.still()
time.sleep(1)

time.sleep(2)
#os.system("flite -t 'Bravo Task started'")
while 1:
    value = int(FrontSensor.getLastEvent())
    if(value >= 2000):  #3000 millimeters
        print(FrontSensor.getLastEvent())
        kit.servo[1].angle = 80


    if(value <= 2000):
        KitMotor.still()

        #os.system("flite -t 'Bravo Task ended'")

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