"""EE 250L Lab 04 Starter Code
Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
import sys

button = 3
ultrasonic_ranger = 4
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    #subscribe to the ultrasonic ranger topic here
    client.subscribe("raspberrypi/custom_callback")
    client.message_callback_add("raspberrypi/custom_callback",custom_callback)
    client.message_callback_add("raspberrypi/custom_callback_led",custom_callback_led)
    client.message_callback_add("raspberrypi/custom_callback_button",custom_callback_button)
    client.subscribe("raspberrypi/led")
    client.subscribe("raspberrypi/ultrasonicRanger")
    client.subscribe("raspberrypi/button")
    #client.subscribe("raspberrypi/led")
#Default message callback. Please use custom callbacks.
def custom_callback(client, userdata, message):
    #if isinstance(int(str(message.payload,"utf-8")),int):
    if message.topic == "raspberrypi/ultrasonicRanger":
        print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
        print("custom_callback: message.payload is of type " + str(type(message.payload)))
        print("VM: " + str(message.payload,"utf-8") + " cm")
    if str(message.payload,"utf-8") == "Button pressed!":
        print("Button pressed!")
    if str(message.payload,"utf-8") == "LED_ON":
        print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
        print("custom_callback: message.payload is of type " + str(type(message.payload)))
    if str(message.payload,"utf-8") == "LED_OFF":
        print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
        print("custom_callback: message.payload is of type " + str(type(message.payload)))

def custom_callback_led(client, userdata, message):
    if str(message.payload,"utf-8") == "LED_ON":
        print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
        print("custom_callback: message.payload is of type " + str(type(message.payload)))
    if str(message.payload,"utf-8") == "LED_OFF":
        print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
        print("custom_callback: message.payload is of type " + str(type(message.payload)))

def custom_callback_button(client,userdata,message):
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
    client.on_message = custom_callback_button
    client.on_message = custom_callback_led
    client.on_message = custom_callback
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        #print("delete this line")
        time.sleep(1)




