#Program for generating values from 1 to n-1 values by using threads
#NumberGenOopsEx3.py
#Generating this example with Object oriented programming languages
#By using constructor
import threading,time
class Numbers:
    def __init__(self,n):
        self.n=n
    def generate(self):
        if(self.n<=0):
            print("{}---->{} is invalid input".format(threading.current_thread().name,self.n))
        else:
            print("*"*50)
            print("Numbers within:{}".format(self.n))
            print("*"*50)
            for val in range(1,self.n+1):
                print("{}---->Value:{}".format(threading.current_thread().name,val))
                time.sleep(0.25)
            print("*"*50)
#MAin program
no=Numbers(int(input("Enter how many numbers you want to generate:")))#Object Creation----Makes to call parameterized constructor
t1=threading.Thread(target=no.generate)
t1.start()