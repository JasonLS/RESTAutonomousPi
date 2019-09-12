import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leftLinesensor = 20  
rightLinesensor = 26

GPIO.setup(leftLinesensor, GPIO.IN)
GPIO.setup(rightLinesensor, GPIO.IN) 

def detect(lineSensor):
    inputValue = GPIO.input(lineSensor)
    if inputValue == 1:
        print("line Detected")
    elif inputValue == 0:
        print("No line Detected")
    return inputValue

def detectLeft():
    detect(leftLinesensor)
    
def detectRight():
    detect(rightLinesensor)