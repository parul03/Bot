import tkinter as tk  
from functools import partial
from textblob import TextBlob       
import pyttsx3        
def call_result(label_result, n1):
    num1 = (n1.get())
       
    # testing 
    engine.say("My mail is  " + num1) 
    engine.say("Thank you, Geeksforgeeks") 
    engine.runAndWait()
    
    gfg = TextBlob(num1) 
  
# using TextBlob.sentiment method 
    gfg = gfg.sentiment
    k=list(gfg)
    if k[0]>0:
        label_result.config(text="Send the mail")
        engine.say("Send the mail")
        engine.runAndWait()
    
    else:
        label_result.config(text="Do not send")
        engine.say("do not send")
        engine.runAndWait()
    return  
       
root = tk.Tk()  
root.geometry('400x200+100+200')  
engine = pyttsx3.init()      
root.title('Send happy Mails')  
engine.say("Welcome to Send happy mails")
engine.runAndWait()       
number1 = tk.StringVar()  
  
      
labelNum1 = tk.Label(root, text="Enter you text here").grid(row=1, column=0)  
      
 
      
labelResult = tk.Label(root)  
      
labelResult.grid(row=7, column=2)  
      
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
      

      
call_result = partial(call_result, labelResult, number1)  
      
buttonCal = tk.Button(root, text="Do I send?", command=call_result).grid(row=3, column=1)  
      
root.mainloop()   

