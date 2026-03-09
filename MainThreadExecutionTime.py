#Program for showing internal flow of Main thread only with execution time.
#MainThreadExecutionTime.py
import threading,time
def squares(lst):
    for val in lst:
        print("{}-----square({})==>{}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)
def cubes(lst):
    for val in lst:
        print("{}-----Cube({})==>{}".format(threading.current_thread().name,val,val**3))
        time.sleep(1)

#Main program
bt=time.time()  #Bt is beginning time here
print("==========================================")
print("program execution started by:",threading.current_thread().name)
print("===============================================")
lst=[12,4,5,16,-6,17,19,4,13,45]
squares(lst)
print("===============================================")
cubes(lst)
print("===========================================")
print("Program execution ended by:",threading.current_thread().name)
print("===========================================")
et=time.time() #et is end time
print("Execution of the program with only MainThreads and without sub threads:",(et-bt))