PORT = '/dev/ttyUSB0'                     # Linux

RUNTIME_SECONDS = 100

from maxbotix import USB_ProxSonar
from time import sleep
from Motors import *

class MySensor(USB_ProxSonar):

    def __init__(self, port):

        USB_ProxSonar.__init__(self, port)

    def handleUpdate(self, distanceMillimeters):
        forward()
        if distanceMillimeters <= 2000:
            still()
        

        print('%d mm' % distanceMillimeters)

sensor = MySensor(PORT)

sensor.start()

sleep(RUNTIME_SECONDS)

sensor.stop()
