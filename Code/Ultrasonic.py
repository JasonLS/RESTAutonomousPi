from maxbotix import USB_ProxSonar
from time import sleep

class MySensor(USB_ProxSonar):
    def __init__(self, port):
        
        self.data = [1,2,3,4,5,6,7,8,5000]
        USB_ProxSonar.__init__(self, port)
            
    def handleUpdate(self, distanceMillimeters):
        
        self.data.append(distanceMillimeters)
        self.data.pop(0)

    def getLastEvent(self):
        return self.data[8]
        #print(self.name + ' %d mm' % distanceMillimeters)
   
