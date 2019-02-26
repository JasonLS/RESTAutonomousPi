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

def turn_left():
  print("Left")
  SetAngle(100)


def turn_right():
  print("Right")
  SetAngle(200)


def stop_turning():
  print("Stop Turning")
  SetAngle(150)
