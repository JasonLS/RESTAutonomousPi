PORT = '/dev/ttyUSB0'                     # Linux

from maxbotix import USB_ProxSonar
from time import sleep
from Motors import *
RUNTIME_SECONDS = 10

class MySensor(USB_ProxSonar):

    def __init__(self, port):

        USB_ProxSonar.__init__(self, port)

    def handleUpdate(self, distanceMillimeters):
        print('%d mm' % distanceMillimeters)
        
        if(distanceMillimeters > 600):
            forward()
        else:
            still()
            
        
     
        return distanceMillimeters

sensor = MySensor(PORT)

sensor.start()
sleep(RUNTIME_SECONDS)

    


sensor.stop()

