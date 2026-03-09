#Program for showing internal flow of Sub thread only with execution time.
#SubThreadExecutionTime.py
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
t1=threading.Thread(target=squares,args=(lst,)) #Tuple notation ,
t1.name="Roshan"
print("===============================================")
t2=threading.Thread(target=cubes,args=(lst,))
t2.name="Arisha"
#Dispatch the sub threads or send it
t1.start()
t2.start()
t1.join()
t2.join()
et=time.time() #et is end time
print("Execution of the program with sub threads:",(et-bt))