#Program for showing internal flow of main thread with sub threads
#SubThreadFlowEx.py====>>>Concurrent/Parallel/Simultaneously execution
import threading
def welcome():
     print("Line-4---->welcome() executed by:",threading.current_thread().name)

def hello():
     print("Line-7---->hello() executed by:",threading.current_thread().name)

def hi(val):
     print("Line-10---->hi(),{} executed by{}:".format(val,threading.current_thread().name))

#Main program
print("Line-13--->>Program execution started by:",threading.current_thread().name)
print("-----------------------------------------------")
t1=threading.Thread(target=welcome) #Here t1 is sub thread object whose name is Thread-0
t1.name="Roshan"
print()
t2=threading.Thread(target=hello) #Here t2 is sub thread object whose name is Thread-1
t2.name="Arshad"
print()
t3=threading.Thread(target=hi,args=("Rossum",)) #Here t3 is sub thread object whose name is Thread-2
t3.name="Zaiba"
#Dispatch or send the sub threads to the target functions
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("---------------------------------------")
print("Program executon eneded by:",threading.current_thread().name)