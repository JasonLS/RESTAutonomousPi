port2 = '/dev/ttyUSB1'
PORT = '/dev/ttyUSB2' # run ls/dev/tty* to see which usb ports it is connected to.      
import time
RUNTIME_SECONDS = 1000

from maxbotix import USB_ProxSonar
from time import sleep
data1=[1,2,3,4,5,6,7,8,9]
data2=[1,2,3,4,5,6,7,8,9]

class MySensor(USB_ProxSonar):
  

    def __init__(self, port):
        
        self.data = [1,2,3,4,5,6,7,8,9]
        USB_ProxSonar.__init__(self, port)
         
   
    
    
    def handleUpdate(self, distanceMillimeters):
        
        self.data.append(distanceMillimeters)
        self.data.pop(0)
    def getLastEvent(self):
        return self.data[8]

        #print(self.name + ' %d mm' % distanceMillimeters)
   
