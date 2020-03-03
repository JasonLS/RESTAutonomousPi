import RPi.GPIO as gpio
import time
gpio.setwarnings(False)

def distance():
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)

    gpio.output(12, False)
    
    while gpio.input(16)==0:
        nosig= time.time()


    while gpio.input(16) == 1:
        sig = time.time()

    tl = sig - nosig

    
    distance = tl/0.000058



    #gpio.cleanup()
    
    return distance

    
while(1):
    print(distance())
    
