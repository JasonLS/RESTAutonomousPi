PORT = '/dev/ttyUSB0'                     # Linux
PORT2 = '/dev/ttyUSB1'
PORT3 = '/dev/ttyUSB2'

from maxbotix import USB_ProxSonar
from time import sleep
from Motors import *
RUNTIME_SECONDS = 100

class Sensor1(USB_ProxSonar):

    def __init__(self, port):

        USB_ProxSonar.__init__(self, port)

    def handleUpdate(self, distanceMillimeters):
        print('%d Sensor1 mm' % distanceMillimeters)

        return distanceMillimeters

class Sensor2(USB_ProxSonar):

    def __init__(self, port):

        USB_ProxSonar.__init__(self, port)

    def handleUpdate(self, distanceMillimeters):
        print('%d Sensor2 mm' % distanceMillimeters)
             
        return distanceMillimeters

class Sensor3(USB_ProxSonar):

    def __init__(self, port):

        USB_ProxSonar.__init__(self, port)

    def handleUpdate(self, distanceMillimeters):
        print('%d Sensor3 mm' % distanceMillimeters)
        
     
        return distanceMillimeters


US1 = Sensor1(PORT)
US2 = Sensor2(PORT2)
US3 = Sensor3(PORT3)

sensor.start()
sleep(RUNTIME_SECONDS)

    


sensor.stop()

