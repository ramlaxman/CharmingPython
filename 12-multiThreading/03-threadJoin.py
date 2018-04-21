"""
The next example shows a thread,
which determines, if a number is prime or not.
The Thread is defined with the threading module:
"""

import threading


class PrimeNumber(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number

    """
    Method representing the thread's activity.

    You may override this method in a subclass. The standard run() method
    invokes the callable object passed to the object's constructor as the
    target argument, if any, with sequential and keyword arguments taken
    from the args and kwargs arguments, respectively.
    """
    def run(self):
        counter = 2
        while counter * counter < self.Number:
            if self.Number % counter == 0:
<<<<<<< HEAD
                print("%d is no prime number, because %d = %d * %d" % (
                self.Number, self.Number, counter, self.Number / counter))
                return
            counter += 1
            print("%d is a prime number" % self.Number)
=======
                print ("%d is no prime number, because %d = %d * %d" % (
                self.Number, self.Number, counter, self.Number / counter))
                return
            counter += 1
            print ("%d is a prime number" % self.Number)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd


threads = []
while True:
    input = int(input("number: "))
    if input < 1:
        break

    thread = PrimeNumber(input)
    threads += [thread]


    """
    Start the thread's activity.

    It must be called at most once per thread object. It arranges for the
    object's run() method to be invoked in a separate thread of control.

    This method will raise a RuntimeError if called more than once on the
    same thread object.

    """
    thread.start()

for x in threads:
    x.join()


"""
Wait until the thread terminates.

        This blocks the calling thread until the thread whose join() method is
        called terminates -- either normally or through an unhandled exception
        or until the optional timeout occurs.

        When the timeout argument is present and not None, it should be a
        floating point number specifying a timeout for the operation in seconds
        (or fractions thereof). As join() always returns None, you must call
        isAlive() after join() to decide whether a timeout happened -- if the
        thread is still alive, the join() call timed out.

        When the timeout argument is not present or None, the operation will
        block until the thread terminates.

        A thread can be join()ed many times.

        join() raises a RuntimeError if an attempt is made to join the current
        thread as that would cause a deadlock. It is also an error to join() a
        thread before it has been started and attempts to do so raises the same
        exception.

"""
