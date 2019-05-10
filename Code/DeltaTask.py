import Motors
import Servo
import Ultrasonic
import time
import os

#Teams are challenged to autonomously parallel park their vehicles.. The
#parking spot will be 1.8 meters by 1.1 meters. The other spots will have vehicles
#simulated with other jeeps, storage totes or something similar. Vehicle should indicate
#when it considers itself “parked.” This could be by emitting a sound or some visual
#signal. For full points teams could park their vehicles autonomously following the same
#directions as a student driver—the vehicle may pull forward parallel to the designated
#“parking space”. The vehicle must move in reverse to fit within the chalked out space
#without hitting the car parked in front of and behind the outlined space. Points
#awarded for parking with sensors, less for dead reckoning.

SerialPort1 = '/dev/ttyUSB0'
SerialPort2 = '/dev/ttyUSB1' # run ls/dev/tty* to see which usb ports it is connected to.  
SerialPort3 = '/dev/ttyUSB2'

LeftSensor = Ultrasonic.MySensor(SerialPort1)
CenterSensor = Ultrasonic.MySensor(SerialPort2)
RightSensor = Ultrasonic.MySensor(SerialPort3)

LeftSensor.start()
CenterSensor.start()
RightSensor.start()
Motors.still()

os.system("flite -t 'Delta Task started'")

while 1 :
    
    #print('Left Sensor ', LeftSensor.getLastEvent(), '\t Center Sensor ', CenterSensor.getLastEvent(), '\t Right Sensor ', RightSensor.getLastEvent())
    #time.sleep(1)
    Motors.forward()
    if LeftSensor.getLastEvent() >= 500 and RightSensor.getLastEvent() >= 500:
        #Execute ppark
        Motors.still()
        Motors.forward()
        time.sleep(1)
        Motors.still()
        Servo.turn_left()
        Motors.backward()
        time.sleep(3)
        Servo.center()
        Servo.turn_right()
        Motors.backward()
        time.sleep(2)
        Motors.still()
        Motors.forward()
        time.sleep(2)
        Motors.still()
        Servo.center()
            
        
##    if LeftSensor.getLastEvent() and RightSensor.getLastEvent() <= 1000:
##        print(x)
##        Motors.still()
##        Motors.backward()
##        time.sleep(2)
##        Motors.still()
##    else:
##        Motors.forward()
    
# sensor.stop stops the reading. 
