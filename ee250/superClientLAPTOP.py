import socket
import select
import errno
import time

HEADER_LENGTH = 10

IP = "3.134.118.175"  #public ip adress remember
PORT = 5002
my_username = input("Username: ") # laptop as username 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket made
client_socket.connect((IP, PORT))  # connect to actual server
client_socket.setblocking(False)  #stop limiter

username = my_username.encode('utf-8')  # identitfies user
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')  # header for server
client_socket.send(username_header + username)  # sends information to server to identify self 

while True:
    message = input(f'{my_username} > ')  #identify self 
    if message:
        message = message.encode('utf-8')   #create messag encoding
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')  
        client_socket.send(message_header + message)  # send message

    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)  #receive info
            if not len(username_header):
                print('Connection closed by the server')   
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')  # receive message
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')  #receive messafe
            print(f'{username} > {message}')

    except IOError as e:  #this is to handle errors such as client leaving unsuspectingly
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        continue

    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()


