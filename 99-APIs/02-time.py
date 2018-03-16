"""
A Python program can handle date and time in several ways. Converting between date formats is a common chore for computers. Python's time and calendar modules help track dates and times

Date arithmetic is easy to do with ticks. However, dates before the epoch cannot be represented in this form. Dates in the far future also cannot be represented this way - the cutoff point is sometime in 2038 for UNIX and Windows.
"""
import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

# Getting current time
localtime = time.localtime(time.time())
print ("Local current time :", localtime)

# Getting formatted time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

# Getting calendar for a month
import calendar

localtime = time.localtime(time.time())
cal = calendar.month(localtime.tm_year, localtime.tm_mon)
print ("Here is the calendar for %d:%d : " % (localtime.tm_year, localtime.tm_mon))
print (cal)

# seconds since epoch from localTime
timeE = time.mktime(localtime)
print ("epoch Time : ", timeE)

# Suspends the calling thread for secs seconds.
print ("before sleep ...")
time.sleep(5)
print ("after sleep ...")

# The method strftime() converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print (time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

# The method strptime() parses a string representing a time according to a format. The return value is a struct_time as returned by gmtime() or localtime().
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print ("returned tuple: %s " % struct_time)

