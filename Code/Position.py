import Motors
import Servo
import time

def right():
	Motors.still()
	Servo.turn_right()
	Motors.forward()
	time.sleep(3)
	Motors.still()
	Servo.center()

def left():
	Motors.still()
	Servo.turn_left()
	Motors.forward()
	time.sleep(3)
	Motors.still()
	Servo.center()

def flip():
	Motors.still()
	Servo.turn_right()
	Motors.forward()
	time.sleep(6)
	Motors.still()
	Servo.center()

right()
time.sleep(1)
left()
time.sleep(1)
flip()
