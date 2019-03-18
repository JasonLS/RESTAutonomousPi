import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Servo_Pin = 14

GPIO.setup(Servo_Pin, GPIO.OUT)
pwm=GPIO.PWM(Servo_Pin, 50) #Sets pin 14 at 50Hz. Configures GPIO to PWM
pwm.start(150) #150 = nothing 



def SetAngle(angle): #Formula for exact angles so it always turns the same degrees left and right.
    duty = angle / 18 + 2
    GPIO.output(Servo_Pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(Servo_Pin, False)
    pwm.ChangeDutyCycle(0) #Remove this? NO, this makes it so the servo stops turning. Otherwise, it will continue to turn.

Turn_Value = 2 #2 for neutral/straight 1 for left, 3 for right

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

def cleanup():
    print("Exiting Servo...")
    if Turn_Value == 1:
        SetAngle(200)
        print("Back to neutral...")

    elif Turn_Value == 3:
        SetAngle(100)
        print("Back to neutral...")   

    elif Turn_Value == 2:
        print("Back to neutral...")

    GPIO.cleanup()