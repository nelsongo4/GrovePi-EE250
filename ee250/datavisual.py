import time
import math
import grovepi
from grovepi import*
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')
from grove_rgb_lcd import *
#import datetime as dt
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation

sensor = 4
sound_sensor = 0
led = 5 
grovepi.pinMode(sound_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")
threshold_value = 400
fig=plt.figure()
while True:
    [temp,hum] = grovepi.dht(sensor,0)
    #temp = float(grovepi.temp(sensor))
    #temp = math.ceil(temp)
    if math.isnan(temp) == False and math.isnan(hum) == False:
        print("temp = %.02f humidity = %.02f "%(temp,hum))
    sensor_value = grovepi.analogRead(sound_sensor)

        # If loud, illuminate LED, otherwise dim
    if sensor_value > threshold_value:
        grovepi.digitalWrite(led,1)
    else:
        grovepi.digitalWrite(led,0)

    print("sensor_value = %d" %sensor_value)
    #print("temp =", temp)
    time.sleep(.5)

