---
layout: default
---
> Teams, Dreams and Memes

# Introduction
Hello. This is the "RESTAutonomousPi" project where we take a PowerWheels car, reverse engineer it and make a small computer drive it, instead of a small child. Below are code snippets, Due Dates, and other resources we used and compiled so future teams of REST and others could use an autonomous vehicle with a Raspberry Pi. 

We are open to any and all questions, advice and critiques.

if you have any questions, please email me at jsedluk01@gmail.com Author Jason Sedluk @2019

## Planning

| TODO         | Progress          | Tested |
|:-------------|:------------------|:------ |
| Motors       | Completed         | Works  |
| Steering     | Completed         | Works  |
| Ultrasonics  | Completed         | Works  |
| Pixy         | Completed         | Works  |
| Line Sensors | Testing           | ...    |


### Using PiGPIO for our Motors with forward function example.

```py
import os #launches pigpiod library which lets us communicate with motors
import time #allows us to set delays
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #needed delay to setup
import pigpio #imports GPIO library
Motor_Pin=4 #sets motor pin to pin 4 on BCM, physical pin 5

pi = pigpio.pi(); #Shortcut naming
pi.set_servo_pulsewidth(Motor_Pin, 1500) #Sets a neutral pulse to motors telling it to get ready for communication   

def forward():
    print("Forward")
    pi.set_servo_pulsewidth(Motor_Pin, 1400)
    
```


### Lists of Parts, Where We Got Them, and Why

* * *
#### Base Items
[Base Shell/Motors:] https://amzn.to/2U7uh0P
[RaspberryPi Board (Model B+):] https://amzn.to/2Sr8W0q
[Proto Board:] https://www.adafruit.com/product/1609

#### Motors
Stock Motors
Motor Controller: https://amzn.to/2IvWJGu

#### Sensors
Maxbotix HRUSB-MaxSonar for people/object detection (x3): https://bit.ly/2VncRgV
Pixy2 for color detection: https://amzn.to/2EdOKu8 

##WIP and Add images.
