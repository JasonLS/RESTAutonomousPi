import Motors
from lux import *
import time
import os
#impoer Ultrasonic

#The team’s Autonomous IVD vehicle should demonstrate its awareness and
#attentiveness to its surroundings. The vehicle will completely enter a darkened
#“garage” structure (10 x 10 walled tent with a “doggie door” on either end), sense that
#it is within a parking garage, stop and flash its lights. When the door is opened at the
#other end it continues on the way.

#while True:
    # Visible-only levels range from 0-2147483647 (32-bit)
    #print('Visible light: {0}'.format(visible))
#    if visible >= 300000:
#        print("high")
#    else:
#        print("low")
#    time.sleep(1)
sensor.gain = adafruit_tsl2591.GAIN_LOW

os.system("flite -t 'Echo Task started'")
time.sleep(2)
while 1:
    Motors.forward()
    visible = sensor.visible
    if visible <= 300000:
            #time.sleep(3)
            Motors.still()
            os.system("flite -t 'Its to fucking dark'")
            #Cue
    else:
            pass
