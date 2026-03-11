#Program which will accept a line of text and split into words and display those words after each and every second and also display letters of those words after each and every second using functional programming...
#WordsExampleByFuncProgEx.py
import threading,time
#Functions to print letters...
def display_letters(word):
    for ch in word:
        time.sleep(1)
        print(ch)
#Function to print words....
def display_words(text):
    words=text.split()
    for w in words:
        time.sleep(1)
        print("Word:",w)
        #Thread for letters....
        t=threading.Thread(target=display_letters,args=(w,))
        t.start()
        t.join()
#Main program
line=input("Enter a line of text:")
t1=threading.Thread(target=display_words,args=(line,))
t1.start()
t1.join()