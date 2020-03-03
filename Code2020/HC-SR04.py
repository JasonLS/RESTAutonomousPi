import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)


TRIG = 23
ECHO = 24

print("Measuring Distance...")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Calibrate")
time.sleep(2)

i = 0
while(1):


    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    
    print("Distance: ", distance)
    time.sleep(.1)
    i+=1

GPIO.cleanup()