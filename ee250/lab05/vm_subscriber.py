"""EE 250L Lab 04 Starter Code
Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
#sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
#sys.path.append('../../Software/Python/grove_rgb_lcd')
#from grove_rgb_lcd import *
#import grovepi

button = 3
ultrasonic_ranger = 4
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    #subscribe to the ultrasonic ranger topic here
    client.subscribe("raspberrypy/custom_callback")
    client.message_callback_add("raspberrypi/custom_callback",custom_callback)
    client.subscribe("raspberrypi/led")
    client.subscribe("raspberrypi/ultrasonicRanger")
    client.subscribe("raspberrypi/button")
    #client.subscribe("raspberrypi/led")
#Default message callback. Please use custom callbacks.
def custom_callback(client, userdata, message):
    print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
    print("custom_callback: message.payload is of type " + str(type(message.payload)))
    if isinstance(int(str(message.payload,"utf-8")),int):
        print("VM: " + str(message.payload,"utf-8") + " cm")
    if str(message.payload,"utf-8") == "Button pressed!":
        print("Button pressed!")
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    #client.on_message = on_message
    client.on_connect = on_connect
    client.on_message = custom_callback
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        #print("delete this line")
        time.sleep(1)





