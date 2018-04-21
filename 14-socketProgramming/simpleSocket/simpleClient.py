# this is a simple client program which opens a connection to a given port 12345 and given host. This is very simple to create a socket client using Python's socket module function.

import socket

socketObject = socket.socket()

host = "172.23.23.200"

port = 12345

socketObject.connect((host,port))

<<<<<<< HEAD
print(socketObject.recv(1024))
=======
print (socketObject.recv(1024))
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

socketObject.close()
