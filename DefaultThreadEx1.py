#Program for showing Default Thread present in python program
#DefaultThreadEx1.py
import threading
tname=threading.current_thread().name
print("Default Thread Name=",tname)
noth=threading.active_count()
print("Default Number of threads in python program=",noth)