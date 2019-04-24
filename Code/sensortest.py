import Ultrasonic
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

while 1 : 
    print('Left Sensor ', LeftSensor.getLastEvent(), '\t Center Sensor ', CenterSensor.getLastEvent(), '\t Right Sensor ', RightSensor.getLastEvent())
    time.sleep(1)
    
# sensor.stop stops the reading. 
