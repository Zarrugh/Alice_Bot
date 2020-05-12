#!/usr/bin/python

import _thread as thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except Exception as e:
   print ("Error: unable to start thread")
   print ("Error: "+ str(e))

while 1:
   time.sleep(1)
   print ("main")
   pass
