#Program for showing internal flow of Main Thread
#DefaultThreadFlowEx.py====>>>.Sequential execution..
import threading
def welcome():
     print("Line-4---->welcome() executed by:",threading.current_thread().name)

def hello():
     print("Line-7---->hello() executed by:",threading.current_thread().name)

def hi():
     print("Line-10---->hi() executed by:",threading.current_thread().name)

#Main program
print("Line-13--->>Program execution started by:",threading.current_thread().name)
welcome()
hello()
hi()
print("Program executon eneded by:",threading.current_thread().name)