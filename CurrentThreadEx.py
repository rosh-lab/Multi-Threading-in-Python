#Program for demonstrating current_thread()
#CurrentThreadEx.py
import threading
t=threading.current_thread()
print("Default Thread Information=",t)
print("Default thread name=",t.name)
print("=======OR============")
print("Default Thread Name=",threading.current_thread().name)