import time
from threading import Thread

def sleeper(i):
<<<<<<< HEAD
    print("thread %d sleeps for 5 seconds\n" % i)
    time.sleep(5)
    print("thread %d woke up\n" % i)
=======
    print ("thread %d sleeps for 5 seconds\n" % i)
    time.sleep(5)
    print ("thread %d woke up\n" % i)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

for i in range(8):
    t = Thread(target=sleeper, args=(i,))
    t.start()
