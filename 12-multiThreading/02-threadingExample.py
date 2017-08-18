import time
from threading import Thread

def sleeper(i):
    print "thread %d sleeps for 5 seconds\n" % i
    time.sleep(5)
    print "thread %d woke up\n" % i

for i in range(8):
    t = Thread(target=sleeper, args=(i,))
    t.start()