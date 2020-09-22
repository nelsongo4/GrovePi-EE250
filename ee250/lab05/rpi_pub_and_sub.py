"""EE 250L Lab 04 Starter Code
Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
import grovepi
from grove_rgb_lcd import *
from grovepi import *
button = 2
grovepi.pinMode(button,"INPUT")
led = 3
pinMode(led,"OUTPUT")
ultrasonic_ranger = 4
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    #subscribe to topics of interest here
    client.subscribe("raspberrypi/custom_callback")
    client.message_callback_add("raspberrypi/custom_callback",custom_callback)
    client.subscribe("raspberrypi/ultrasonicRanger")
    client.subscribe("raspberrypi/led")
    client.subscribe("raspberrypi/lcd")
#Default message callback. Please use custom callbacks.
def custom_callback(client, userdata, message):
    print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
    print("custom_callback: message.payload is of type " + str(type(message.payload)))
    if str(message.payload,"utf-8") == "LED_ON":
        digitalWrite(led,1)
    if str(message.payload,"utf-8") == "LED_OFF":
        digitalWrite(led,0)
    if str(message.payload,"utf-8") == "w" or str(message.payload,"utf-8") == "a" or str(message.payload,"utf-8") == "s" or str(message.payload,"utf_8") == "d":
        setText_norefresh(str(message.payload,"utf-8"))
#def custom_callback_led(client,userdata,message):
    #if str(message.payload,"utf-8") == "LED_ON":
        #print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
        #print("custom_callback: message.payload is of type " + str(type(message.payload)))
        #digitalWrite(led,1)
    #if str(message.payload,"utf-8") == "LED_OFF":
        #print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
        #print("custom_callback: message.payload is of type " + str(type(message.payload)))
        #digitalWrite(led,0)

#def custom_callback_lcd(client,userdata,message):
    #if str(mesage.payload,"utf-8") == "w" or str(mesage.payload,"utf-8") == "a" or str(mesage.payload,"utf-8") == "s" or str(mesage.payload,"utf_8") == "d":
        #print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
        #print("custom_callback: message.payload is of type " + str(type(message.payload)))
        #setTextnorefresh(str(message.payload,"utf-8"))

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    #client.on_message = on_message
    client.on_message = custom_callback
    #client.on_message = custom_callback_led
    #client.on_message = custom_callback_lcd
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        #print("delete this line")
        time.sleep(1)
        client.publish("raspberrypi/ultrasonicRanger",grovepi.ultrasonicRead(ultrasonic_ranger))
        if grovepi.digitalRead(button):
            client.publish("raspberrypi/button","Button pressed!")


