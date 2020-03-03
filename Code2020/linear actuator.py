# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
#mode=GPIO.getmode()
#print (" mode ="+str(mode))
GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24



#14 Red Enable
#4 Black IN4
#15 Purple IN3

enable=14
forward=18
backward=4

#StepPinForward=16
#StepPinBackward=18
sleeptime=1

#GPIO.setmode(GPIO.BOARD)
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(forward, GPIO.OUT)
GPIO.setup(backward, GPIO.OUT)


#GPIO.setup(StepPinForward, GPIO.OUT)
#GPIO.setup(StepPinBackward, GPIO.OUT)

def forwardmotor(x):
    #GPIO.output(StepPinForward, GPIO.HIGH)
    GPIO.output(enable, GPIO.HIGH)
    
    GPIO.output(forward, GPIO.HIGH)
    GPIO.output(backward, GPIO.LOW)

    print("forwarding running  motor ")
    time.sleep(x)
    GPIO.output(enable, GPIO.LOW)
    #GPIO.output(StepPinForward, GPIO.LOW)

def reversemotor(x):
    #GPIO.output(StepPinBackward, GPIO.HIGH)
    GPIO.output(enable, GPIO.HIGH)
    
    GPIO.output(forward, GPIO.LOW)
    GPIO.output(backward, GPIO.HIGH)

    print ("backward running  motor ")
    time.sleep(x)
    GPIO.output(enable, GPIO.LOW)
    #GPIO.output(StepPinBackward, GPIO.LOW)

print ("forward motor ")
#forwardmotor(5)
print ("reverse motor")
reversemotor(5)

print ("Stopping motor")
GPIO.cleanup()