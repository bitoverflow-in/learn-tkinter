# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:51:36 2019

@author: Durlav
"""

from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
#all the user input will be stored in operator as a string 
#text_Input.set(operator) will show the operator string in the entry field 
def btnClear():
    global operator
    operator=""
    text_Input.set("")
#astext_Input.set() and operator are given the value of "" they will store nothing and work as a clear button     
def btnEquals():
    global operator
    result=str(eval(operator))
    text_Input.set(result)
    operator=""
#eval will evaluate all the calculation there is in operator and provide result.
cal=Tk()
#cal is the window

cal.title("Calculator")
#title of the window

operator=""
#operator is a string , it will store everything written on the entry field as a string
text_Input = StringVar ()
#this will convert entry to string 

entryField = Entry(cal,font=('ariel',20,'bold'), textvariable = text_Input,bd=30,insertwidth=3,bg="royalblue",justify="right")
entryField.grid(columnspan=4)
#Entry is used to take user input 

button7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="7",command=lambda:btnClick(7))
button7.grid(row=1,column=0)
button8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="8",command=lambda:btnClick(8))
button8.grid(row=1,column=1)
button9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="9",command=lambda:btnClick(9))
button9.grid(row=1,column=2)
buttonAdd = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="+",command=lambda:btnClick("+"))
buttonAdd.grid(row=1,column=3)


button4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="4",command=lambda:btnClick(4))
button4.grid(row=2,column=0)
button5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="5",command=lambda:btnClick(5))
button5.grid(row=2,column=1)
button6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="6",command=lambda:btnClick(6))
button6.grid(row=2,column=2)
buttonSub = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="-",command=lambda:btnClick("-"))
buttonSub.grid(row=2,column=3)


button1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="1",command=lambda:btnClick(1))
button1.grid(row=3,column=0)
button2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="2",command=lambda:btnClick(2))
button2.grid(row=3,column=1)
button3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="3",command=lambda:btnClick(3))
button3.grid(row=3,column=2)
buttonMul = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="*",command=lambda:btnClick("*"))
buttonMul.grid(row=3,column=3)


button0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="0",command=lambda:btnClick(0))
button0.grid(row=4,column=1)
buttonc = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="c",command=btnClear)
buttonc.grid(row=4,column=0)
buttondiv = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="/",command=lambda:btnClick("/"))
buttondiv.grid(row=4,column=3)
buttonEqual = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('ariel',20,'bold'),text="=",command=btnEquals)
buttonEqual.grid(row=4,column=2)


cal.mainloop()