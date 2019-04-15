---
layout: default
---
> R.E.S.T club is a forging ground for the tech leaders of tomorrow
>                                    -Rasul Mahones (Mentor)

# Introduction
Hello. This is the "RESTAutonomousPi" project where we take a PowerWheels car, reverse engineer it and make a small computer drive it, instead of a small child. Below are code snippets, Due Dates, and other resources we used and compiled so future teams of REST and others could use an autonomous vehicle with a Raspberry Pi. 

[For videos of our car, outreace or to contact us, please visit](inaction.md)


## Planning

| TODO         | Progress          | Tested |
|:-------------|:------------------|:------ |
| Motors       | Completed         | Works  |
| Steering     | Completed         | Works  |
| Ultrasonics  | Completed         | Works  |
| Pixy         | Completed         | Works  |
| Line Sensors | Testing           | ...    |

### Lists of Parts, Where We Got Them, and Why

* * *
#### Base Items
Base Shell/Motors: [Powerwheels Jeep](https://amzn.to/2U7uh0P)

Microcomputer Controlling the whole car: [RaspberryPi Board (Model B+)](https://amzn.to/2Sr8W0q)

Wiring connection [Proto Board](https://www.adafruit.com/product/1609)

#### Motors
(Stock Motors)

Motor Controller: [Velineon ESC from R/C car](https://amzn.to/2IvWJGu)

Servo: [Hitec HS-785HB w/ Gearbox](https://bit.ly/2GqXIX9)


#### Sensors
Ultrasonic sensors(x3): [Maxbotix HRUSB-MaxSonar](https://bit.ly/2VncRgV)

Color Tracking Camera: [Pixy2](https://amzn.to/2EdOKu8) 

Line Tracking Sensors(x4): [Gikfun IR Sensor](https://amzn.to/2v3KFob) 

#### Batteries
Motor Battery [11.1v, 5A, 4s](https://amzn.to/2ZhBmPt)

Servo Battery [7.4v, 1A, 3s](https://amzn.to/2UZbhoH)

RaspberryPi/LCD Battery [Any long lasting portable charger will do](https://amzn.to/2VH4UDL)

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

### Issues
Problem: Motors would "jerk" forwards when turning the servo
Solution: Instead of powering the servo through the ESC, we powered it seperately through a LiPo

