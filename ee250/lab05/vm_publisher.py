"""EE 250L Lab 04 Starter Code
Run vm_publisher.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from pynput import keyboard

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    #subscribe to topics of interest here
    #client.subscribe("raspberrypy/custom_callback")
    #client.message_callback_add("raspberrypi/custom_callback",custom_callback)
    #client.subscribe("raspberrypi/led")

#Default message callback. Please use custom callbacks.
def custom_callback(client, userdata, message):
    print("Custom_callback: " + message.topic + " " + "\"" + str(message.payload, "utf-8") + "\"")
    print("custom_callback: message.payload is of type " + str(type(message.payload)))

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def on_press(key):
    try: 
        k = key.char # single-char keys
    except: 
        k = key.name # other keys
    
    if k == 'w':
        print("w")
        #send "w" character to rpi
        client.publish("raspberrypi/lcd","w")
    elif k == 'a':
        print("a")
        # send "a" character to rpi
        client.publish("raspberrypi/lcd","a")
        #send "LED_ON"
        client.publish("raspberrypi/led","LED_ON")
    elif k == 's':
        print("s")
        # send "s" character to rpi
        client.publish("raspberrypi/lcd","s")
    elif k == 'd':
        print("d")
        # send "d" character to rpi
        client.publish("raspberrypi/lcd","d")
        # send "LED_OFF"
        client.publish("raspberrypi/led","LED_OFF")
if __name__ == '__main__':
    #setup the keyboard event listener
    lis = keyboard.Listener(on_press=on_press)
    lis.start() # start to listen on a separate thread

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
