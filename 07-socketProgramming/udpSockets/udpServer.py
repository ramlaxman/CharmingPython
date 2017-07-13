import socket
from datetime import datetime
import time

hostname = "172.23.23.200"
portNo = 50000


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    time.sleep(5)
    message = "this is udp stream at : %s" % str(datetime.now())
    print message
    sock.sendto(message, (hostname, portNo))

