from evdev import InputDevice, categorize, ecodes
import Motors
import Servo
import Ultrasonic
import os

LT=310
RT=311
LB=308
RB=309
LR=16
UPDN=17
A=306
X=307
Y=304
B=305
START=313
SEL=312

HOME=316
LS=314
RS=315

LX = 0
LY = 1

up = 46
down = 32
left = 18
right = 33

RX = 2
RY = 5


#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0') #Change this if keyboard or mouse plugged in
print(gamepad)

for event in gamepad.read_loop():

    if event.type == ecodes.EV_ABS:
        if event.value == 0:
            if event.code == LX:
                print("leftstick left")
                Servo.turn_left()
            elif event.code == LY:
                print("leftstick up")
            elif event.code == RX:
                print("rightstick left")
            elif event.code == RY:
                print("rightstick up")
                

        elif event.value == 255:
            if event.code == LX:
                print("leftstick right")
                Servo.turn_right()
            elif event.code == LY:
                print("leftstick down")
            elif event.code == RX:
                print("rightstick right")
            elif event.code == RY:
                print("rightstick down")

        elif event.value == 1:
            if event.code == UPDN:
                print("down")
            elif event.code == LR:
                print("right")

        elif event.value == -1:
            if event.code == UPDN:
                print("up")
            elif event.code == LR:
                print("left")
    
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == Y:
                print("Y")
                
            elif event.code == B:
                print("B")
                  
            elif event.code == A:
               print("A")
               #os.system("python test.py")
            elif event.code == X:
                print("X")

            elif event.code == START:
                print("start")
            elif event.code == SEL:
                print("select")
            elif event.code == HOME:
                print("home")
            elif event.code == LS:
                print("Left Click")
            elif event.code == RS:
                print("Right Click")

            elif event.code == RB:
                print("right bumper")
            elif event.code == LB:
                print("left bumper")

            elif event.code == LT:
                print("left trigger")
                Motors.forward()
            elif event.code == RT:
                print("right trigger")
                Motors.backward()



    
