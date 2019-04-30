import Ultrasonic
import Motors
import Servo
import time
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

while 1 : 
    #print('Left Sensor ', LeftSensor.getLastEvent(), '\t Center Sensor ', CenterSensor.getLastEvent(), '\t Right Sensor ', RightSensor.getLastEvent())
    #time.sleep(1)
    if LeftSensor.getLastEvent() <= 1000:
        print("Forward Detect")
        Motors.forward()
        if LeftSensor.getLastEvent() <= 1000 and RightSensor.getLastEvent() >= 1000:
            #Execute ppark
            Motors.still()
            Motors.forward()
            time.sleep(1)
            Motors.still()
            Servo.turn_left()
            Motors.backward()
            time.sleep(1)
            Servo.center()
            Servo.turn_right()
            Motors.backward()
            time.sleep(.5)
            Motors.still()
            Motors.forward()
            time.sleep(.5)
            Motors.still()
            
        
##    if LeftSensor.getLastEvent() and RightSensor.getLastEvent() <= 1000:
##        print(x)
##        Motors.still()
##        Motors.backward()
##        time.sleep(2)
##        Motors.still()
##    else:
##        Motors.forward()
    
# sensor.stop stops the reading. 
