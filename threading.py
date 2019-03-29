
import _thread
import time


def hello( threadName):
    hello_count = 0
    for i in range (1,6):
        print("Hello "+threadName+str(hello_count)+"\n")
        hello_count+=1
        time.sleep(1)
        print("I"+_thread._count())


def hi(threadName):
    hi_count = 0
    for i in range(1,6):
        print("Hi "+threadName +str(hi_count)+"\n")
        hi_count+=1
        time.sleep(2)
        print(_thread._count())

try:
    t1 =_thread.start_new_thread( hello, ("Thread", ))
    t1 = _thread.start_new_thread( hi, ("Thread", ))

except:
   print("Error: unable to start thread")

while 1:
   pass

