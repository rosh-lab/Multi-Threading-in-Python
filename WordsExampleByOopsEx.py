#Program which will accept a line of text and split into words and display those words after each and every second and also display letters of those words after each and every second using Object oriented  programming...
#WordsExampleByOopsEx.py
import threading,time
class TextProcessor:
    def display_letters(self,word):
        for ch in word:
            time.sleep(1)
            print(ch)
    def display_words(self,text):
        words = text.split()
        for w in words:
            time.sleep(1)
            print("Word:", w)
            t = threading.Thread(target=self.display_letters, args=(w,))
            t.start()
            t.join()
#Main program
line=input("Enter a line of text:")
obj=TextProcessor()
t1=threading.Thread(target=obj.display_words,args=(line,))
t1.start()
t1.join()