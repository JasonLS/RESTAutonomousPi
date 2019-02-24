import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)


servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 14) # GPIO 14 for PWM with 50Hz
p.start(0) # Initialization

def turn_left():
  print("Left")
  p.ChangeDutyCycle(20)

def turn_right():
  print("Right")
  p.ChangeDutyCycle(1)

def stop_turning():
  print("Turn Stop")
  p.ChangeDutyCycle(0)    

  
