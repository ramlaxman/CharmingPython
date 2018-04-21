"""
It is also possible to use a list as a queue,
where the first element added is the first element retrieved (first-in, first-out);
however, lists are not efficient for this purpose.
While appends and pops from the end of list are fast,
doing inserts or pops from the beginning of a list is slow
(because all of the other elements have to be shifted by one)
"""

# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:

from collections import deque
print("define queue : ")
queue = deque(["Eric", "John", "Michael"])
print("queue defined : ", queue)

print("add element to queue")
queue.append("Terry")           # Terry arrives

print("add element to queue")
queue.append("Graham")          # Graham arrives

print("remove element from queue")
queue.popleft()                 # The first to arrive now leaves

print("remove element from queue")
queue.popleft()                 # The second to arrive now leaves

print("final queue : ", queue)                           # Remaining queue in order of arrival

