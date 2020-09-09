"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
repo link :https://github.com/nelsongo4/GrovePi-EE250/edit/master/ee250/lab03/tcp_client.py
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket
#my ec2 ip address
HOST = '52.15.134.140' 
PORT = 5002

def main():
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    # TODO: Get user input and send it to the server using your TCP socket
    sent_msg = input("Enter message: ")
    s.send(str.encode(sent_msg))
    # TODO: Receive a response from the server and close the TCP connection
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    s.close()
if __name__ == '__main__':
    main()
