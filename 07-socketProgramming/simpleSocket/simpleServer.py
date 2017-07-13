# this is an example of a simple socket server

import socket

socketObject = socket.socket()

host = socket .gethostname()

print host

port = 12345

socketObject.bind((host,port))

socketObject.listen(5)

while True:
    connectionObject, address = socketObject.accept()
    print "Got connection from : ", address
    connectionObject.send("Thank you for connecting")
    connectionObject.close()

