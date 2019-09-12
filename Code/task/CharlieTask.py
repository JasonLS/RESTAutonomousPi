import RPi.GPIO as GPIO
import Motors
import Servo
import os

#Highly reflective tape will be used to define lanes (of proportional accuracy to the
#vehicle and real world). The course will include approximately 3-5 meters of straightaway
#followed by 3-5 meters of S-turns, etc. Team vehicles must indicate with visual,
#auditory, or tactile cues/warnings if straying too close to “edge of road.”

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN) #Right
GPIO.setup(26, GPIO.IN) #Left

GPIO.setwarnings(False)
still()

os.system("flite -t 'Charlie Task Started'")

#Test First
while GPIO.input(26) and GPIO.input(20) != 1:
    forward()
    if GPIO.input(26) == 1:
        print("Detected")
        still()
    elif GPIO.input(20) == 1:
        print("Detected")
        still()

#What should work
#while GPIO.input(26) and GPIO.input(20) != 1:
#    forward()
#    if GPIO.input(26) == 1:
#        print("Left Detected")
#        Servo.turn_right()
#        time.sleep(1)
#        break

#    elif GPIO.input(20) == 1:
#        print("Right Detected")
#        still()
#        Servo.turn_left()
#        time.sleep(1)
#        break
