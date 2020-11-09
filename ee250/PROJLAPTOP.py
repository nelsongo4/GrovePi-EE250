import socket
#import threading
import time
import math

HOST = '172.31.30.76'
HOST = '18.218.6.170'
#HOST ='0.0.0.0'
PORT = 5002        # The port used by the server

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))  
    print('success')
    # TODO: Get user input and send it to the server using your TCP socket
    while True:
        #sent_msg = input("Enter message: ")
        # TODO: Receive a response from the server and close the TCP connection
        msg = s.recv(1024)
        print(msg.decode("utf-8"))
        s.close()

if __name__ == '__main__':
    main()
