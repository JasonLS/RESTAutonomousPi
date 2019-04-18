import oof
import time
SerialPort1 = '/dev/ttyUSB2'
SerialPort2 = '/dev/ttyUSB1' # run ls/dev/tty* to see which usb ports it is connected to.  

LeftSensor = oof.MySensor(SerialPort1)
RightSensor = oof.MySensor(SerialPort2)

LeftSensor.start()
RightSensor.start()

while 1 : 
    print('Left Sensor ', LeftSensor.getLastEvent(), '\t Right Sensor ', RightSensor.getLastEvent())
    time.sleep(1)
#call .stop() for cleanup

