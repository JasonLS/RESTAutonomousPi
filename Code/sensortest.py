import Ultrasonic
import time
SerialPort1 = '/dev/ttyUSB0' # Type ls/dev/tty in the terminal then tab to see which usb ports are connected be default, 0-2 will be for US. 
SerialPort2 = '/dev/ttyUSB1'  
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
    
# LeftSensor.stop stops the reading for the Left Sensor
