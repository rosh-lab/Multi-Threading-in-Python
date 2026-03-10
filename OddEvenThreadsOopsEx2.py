#Program for creating two sub threads for generating odd and even numbers within the range..
#OddEvenThreadsOopsEx2.py
#BY using Object oriented approach
import threading,time
class Odd:
    def odd(self,n):
        if(n<=0):
            print("{}----->{} is invalid input".format(threading.current_thread().name,n))
        else:
            for val in range(1,n+1,2):
                print("{}----->Odd Number:{}".format(threading.current_thread().name,val))
                time.sleep(1)
class Even:
    def even(self,n):
        if(n<=0):
            print("{}----->{} is invalid input".format(threading.current_thread().name,n))
        else:
            for val in range(2,n+1,2):
                print("{}----->Even Number:{}".format(threading.current_thread().name,val))
                time.sleep(1)
#Main program...
t1=threading.Thread(target=Odd().odd,args=(10,)) #Nameless object
t2=threading.Thread(target=Even().even,args=(10,))
t1.start()
t2.start()
