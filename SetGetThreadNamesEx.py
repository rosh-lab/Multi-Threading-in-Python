#Program for demonstrating set and get the threads names
#SetGetThreadNamesEx.py
import threading
def welcome():
     print("\tLine-5---->welcome() executed by:",threading.current_thread().name)

#Main program
print("--------------------------------------------------")
print("Line-9--->>Program execution started by:",threading.current_thread().name)
print("-----------------------------------------------")
t1=threading.Thread(target=welcome) #Here t1 is object name and called sub thread
#Here the default name to the sub thread is Thread-1
#print("In main program sub Thread name=",t1.getName()) #It will give Thread-1 and gives deprication warning means getName() is changed to simply name ....deprication meaing changed
#NOt recommemdded to use this getName()
print("In main program sub thread name=",t1.name)
#t1.setName("RS") #setName is also depricated means changed ...simpliy write t1.name
#NOt recommended to write this also setName()
t1.name="RS"  #Setting the name to the sub thread
print("In main program sub thread name=",t1.name)
t1.start()
print("--------------------------------------------")
print("-----------------------------------------------")