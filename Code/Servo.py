import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Servo_Pin = 4

GPIO.setup(Servo_Pin, GPIO.OUT)
pwm=GPIO.PWM(Servo_Pin, 60) #Sets pin 14 at 50Hz. Configures GPIO to PWM
pwm.start(0) #150 = nothing
#Turn_Value = 0

def SetAngle(angle): #Formula for exact angles so it always turns the same degrees left and right.
    angle /= 18
    angle += 2
    
    GPIO.output(Servo_Pin, True)
    pwm.ChangeDutyCycle(angle)
    time.sleep(1)
    GPIO.output(Servo_Pin, False)
    
    pwm.ChangeDutyCycle(0) #Remove this? NO, this makes it so the servo stops turning. Otherwise, it will continue to turn.

#Turn_Value = 1
def turnLeft():
    #global Turn_Value
    print("Left")
    SetAngle(100)
    
    #Turn_Value =  1
    
    #if Turn_Value != 1 and Turn_Value != 3:
    #    print("Left")
    #    SetAngle(100)
    #    Turn_Value =  1

#Turn_Value = 3
def turnRight():
    #global Turn_Value
    
    print("Right")
    SetAngle(200)
    #Turn_Value = 3
    
    #if Turn_Value != 3 and Turn_Value != 1:
    #    print("Right")
    #    SetAngle(200)
    #    Turn_Value = 3

    
#Turn_Value = 2
def turnStraight():
    global Turn_Value

    if Turn_Value != 2:
        print("Centering")
        if Turn_Value == 1: #Left
            turnRight()
            Turn_Value = 2
        elif Turn_Value == 3: #Right
            turnLeft()
            Turn_Value = 2
        
def cleanup():
    global Turn_Value
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

turnLeft()
time.sleep(1)
turnRight()
time.sleep(1)
turnRight()
time.sleep(1)
turnLeft()

time.sleep(1)
GPIO.cleanup()
#cleanup()