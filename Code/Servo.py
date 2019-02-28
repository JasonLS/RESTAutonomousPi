import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

servoPIN = 14

GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN, 50) #Sets pin 14 at 50Hz
pwm.start(150) #150 = nothing 



def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoPIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    pwm.ChangeDutyCycle(0) #Remove this? NO, this makes it so the servo stops turning after 1 second

#while 1:
#    val = int(input("Input value: \n"))
#    if(val > 0):
#        SetAngle(val)
#    else:
#        break
# Testing
Turn_Value = 2 #2 for neautral/straight 1 for left, 3 for right
def turn_left():
    if Turn_Value != 1:
        print("Left")
        SetAngle(100)
        Turn_Value =  1

def turn_right():
    if Turn_Value != 3:
        print("Right")
        SetAngle(200)
        Turn_Value = 3

def stop_turning():
    if Turn_Value != 2:
        print("Stop Turning")
        SetAngle(150)
        Turn_Value = 2
