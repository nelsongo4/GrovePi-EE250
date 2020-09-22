"""EE 250L Lab 04 Starter Code
Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
import grovepi
button = 2
led = 3
ulltrasonic_ranger = 4
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    #subscribe to topics of interest here
    client.subscribe("raspberrypy/custom_callback")
    client.message_callback_add("raspberrypi/custom_callback",custom_callback)
    client.subscribe("raspberrypi/ultrasonicRanger")
    client.subcribe("raspberrypi/led")
    client.subscribe("raspberrypi/lcd")
#Default message callback. Please use custom callbacks.
def custom_callback(client, userdata, message):
    print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
    print("custom_callback: message.payload is of type " + str(type(message.payload)))
    if str(message.payload,"utf-8") == "LED_ON":
        digitalWrite(led,1)
    if str(message.payload,"utf-8") == "LED_OFF":
        digitalWrite(led,0)
    if str(mesage.payload,"utf-8") == "w" or str(mesage.payload,"utf-8") == "a" or str(mesage.payload,"utf-8") == "s" or str(mesage.payload,"utf_8") == "d":
        setTextnorefresh(str(message.payload,"utf-8"))

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    #client.on_message = on_message
    client.on_message = custom_callback
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        #print("delete this line")
        time.sleep(1)
        client.publish("raspberrypi/ultrasonicRanger",grovepi.ultrasonicRead(ultrasonic_ranger))
        if grovepi.pinMode(button,"INPUT") == 0:
            client.publish("raspberrypi/button","Button pressed!")



