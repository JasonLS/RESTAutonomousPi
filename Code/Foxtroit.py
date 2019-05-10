import serial  # pyserial is required
from micropyGPS import MicropyGPS #https://github.com/inmcm/micropyGPS

gps = MicropyGPS()
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=30)
sent = uart.readline().decode('utf-8')

while 1:
    sent = uart.readline().decode('utf-8')
    print(sent)
    for x in sent:
        gps.update(x)
    print("fix_type 1 means no fix: ",gps.fix_type)
    print("lat " ,gps.latitude)
    print("long " ,gps.longitude)
    print("speed ", gps.speed)
    print("satellites_visible " ,gps.satellites_visible())
    print("direction ", gps.compass_direction())
    
