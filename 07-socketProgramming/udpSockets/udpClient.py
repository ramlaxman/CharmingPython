import socket

hostname = ""
portNo = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((hostname, portNo))
print "bind success"
while True:
	print "receiving"
	data, addr = sock.recvfrom(1024)
	print "raceived data : ", data
	print "received addr : ", addr
