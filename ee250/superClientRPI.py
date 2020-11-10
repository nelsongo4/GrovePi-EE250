import socket
import select
import errno
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
grovepi.pinMode(sound_sensor,"INPUT")  #sound sensor is input
grovepi.pinMode(led,"OUTPUT") # led outputs light
threshold_value = 400  # threshold for when light turns on
HEADER_LENGTH = 10

IP = "3.134.118.175" #publlic ip
PORT = 5002
my_username = input("Username: ") # rpi as username 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    [temp,hum] = grovepi.dht(sensor,0)
    #temp = float(grovepi.temp(sensor))
    #temp = math.ceil(temp)
    #if math.isnan(temp) == False and math.isnan(hum) == False:
        #print("temp = %.02f humidity = %.02f "%(temp,hum))
    #    temp = temp
    #    hum = hum
    sensor_value = grovepi.analogRead(sound_sensor)

        # If loud, illuminate LED, otherwise dim
    if sensor_value > threshold_value:
        grovepi.digitalWrite(led,1)
    else:
        grovepi.digitalWrite(led,0)

    print("sensor_value = %d" %sensor_value)
    #print("temp =", temp)
    time.sleep(.5)
    print(f'{my_username} > ')
    if math.isnan(temp) == False and math.isnan(hum) == False:
        #print("temp = %.02f humidity = %.02f "%(temp,hum))
        message = str(temp)
        print(message)
    else:
        message = " "
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            print(f'{username} > {message}')

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        continue

    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()

