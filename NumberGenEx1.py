#Program for generating values from 1 to n-1 values by using threads
#NumberGenEx1.py
#Generating this example with functional approach
import threading,time
def generate(n):
    if(n<=0):
        print("{}---->{} is invalid input".format(threading.current_thread().name,n))
    else:
        print("*"*50)
        print("Numbers within:{}".format(n))
        print("*"*50)
        for val in range(1,n+1):
            print("{}---->Value:{}".format(threading.current_thread().name,val))
            time.sleep(1)
        print("*"*50)
#MAin program
n=int(input("Enter how many numbers you want to generate:"))
t1=threading.Thread(target=generate,args=(n,))
t1.start()
