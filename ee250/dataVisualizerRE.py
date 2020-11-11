import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
import math
import grovepi
from grovepi import*
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')
from grove_rgb_lcd import *

sensor = 4
sound_sensor = 0
led = 5
grovepi.pinMode(sound_sensor,"INPUT")      #indicates sound sensor
grovepi.pinMode(led,"OUTPUT")      #indicates led
threshold_value = 500    #init threshold for sound sensor
fig = plt.figure()    #ceates figure
ax = fig.add_subplot(1, 1, 1)    # creates loaction for plt
xs = []    # init arr
ys = []    #init arr


def animate(i, xs, ys):
    [temp, hum] = grovepi.dht(sensor, 0)
    # add x and y to lists
    if math.isnan(temp) is False and math.isnan(hum) is False:
        print("temp = %.02f humidity = %.02f " % (temp, hum))
    sensor_value = grovepi.analogRead(sound_sensor)

    # If loud, illuminate LED
    if sensor_value > threshold_value:
        grovepi.digitalWrite(led, 1)
    else:
        grovepi.digitalWrite(led, 0)

    print("sensor_value = %d" % sensor_value)
    # print("temp =", temp)
    time.sleep(.5)
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))    # this will create time
    ys.append(temp)    # adds to arr
    xs = xs[-30:]
    ys = ys[-30:]
    ax.clear()
    ax.plot(xs, ys)   # plot data
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature vs Time')   # name of plot
    plt.ylabel('Temperature C')  # y label


ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=4000)   #creates animation using library

plt.show()   # shows graphs being updated

