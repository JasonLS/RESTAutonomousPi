import Motors
import lux
#impoer Ultrasonic

#The team’s Autonomous IVD vehicle should demonstrate its awareness and
#attentiveness to its surroundings. The vehicle will completely enter a darkened
#“garage” structure (10 x 10 walled tent with a “doggie door” on either end), sense that
#it is within a parking garage, stop and flash its lights. When the door is opened at the
#other end it continues on the way.

while True:
    #lux = sensor.lux
    # Visible-only levels range from 0-2147483647 (32-bit)
    visible = lux.sensor.visible
    #print('Visible light: {0}'.format(visible))
    if visible >= 300000:
        print("high")
    else:
        print("low")
    time.sleep(1)

#while visible >= 300000:
#	Motors.forward()
#	if visible <= 300000:
#		time.sleep(3)
#		Motors.still()
		#Cue
#	else:
#		pass