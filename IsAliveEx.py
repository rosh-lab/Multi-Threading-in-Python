#Program for showing Execution status of sub threads
#IsAliveEx.py
import threading,time
def squares(lst):
    for val in lst:
        print("{}-----square({})==>{}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)
#Main program
bt=time.time()  #Bt is beginning time here
print("==========================================")
print("program execution started by:",threading.current_thread().name)
print("===============================================")
lst=[12,4,5,16,-6,17,19,4,13,45]
t1=threading.Thread(target=squares,args=(lst,))
print("Execution Status of t1 before start()=",t1.is_alive())
print("Number of active threads before start=",threading.active_count())#1
t1.start()
print("Execution Status of t1 after start()=",t1.is_alive())
print("Number of active threads after start=",threading.active_count())#2