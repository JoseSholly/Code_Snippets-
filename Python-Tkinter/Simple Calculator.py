# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 08:57:25 2021

@author: JOSE SHOLLY
"""
from math import factorial, sin,pi,radians,tan,cos,sqrt,log,exp,factorial,atan,asin,acos,degrees
from tkinter import *
from tkinter.messagebox import *
def quitter_function(): 
    answer = askquestion(title='Quit?', message='Really quit?') 
    if answer=='yes': 
        root.destroy()
def button_click(number):
    current= entry.get()
    entry.delete(0,END)
    
    entry.insert(0,str(current)+str(number))

def button_clear():
    
    entry.delete(0,END)
    #entry.insert(0,0)

def button_add():
    first_number= entry.get()
    global f_num
    global math
    math= "addition"
    f_num= float(first_number)
    entry.delete(0,END)  

def button_equal():
    second_number= eval(entry.get())
    entry.delete(0,END)
    if math=="addition":
        entry.insert(0, f_num+second_number)
    elif math== "subtraction":
        entry.insert(0, f_num-second_number)
    elif math=="division":
        entry.insert(0, f_num/second_number)
    elif math== "multiplication":
        entry.insert(0, f_num*second_number)
    elif math== "powerN":
        entry.insert(0, f_num**second_number)
    elif math== "squareN":
        entry.insert(0, f_num**(1/second_number))
    #elif math== "pi":
        #entry.insert(0,pi)

def button_subtract():
    first_number= entry.get()
    global f_num
    global math
    math= "subtraction"
    f_num= eval(first_number)
    entry.delete(0,END) 
def button_divide():
    first_number= entry.get()
    global f_num
    global math
    math= "division"
    f_num= eval(first_number)
    entry.delete(0,END) 

def button_multiply():
    first_number= entry.get()
    global f_num
    global math
    math= "multiplication"
    f_num= eval(first_number)
    entry.delete(0,END) 

def button_pop():
    current= list(entry.get())
    current.pop(-1)
    entry.delete(0, END)
    entry.insert(0,"".join(current))

def button__power2():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END)
    entry.insert(0,pow(f_num,2))

def button__powerN():
    first_number= entry.get()
    global f_num
    global math
    math= "powerN"
    f_num= eval(first_number)
    entry.delete(0,END)

def button__sine():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END)
    y= sin(radians(f_num))
    entry.insert(0,y)

def button__cosine():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END)
    y= cos(radians(f_num))
    entry.insert(0,y)

def button__tangent():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END)
    y= tan(radians(f_num))
    entry.insert(0,y)

def button__squ_root():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END) 
    y= sqrt(f_num)
    entry.insert(0,y)

def button__sqrtN():
    first_number= entry.get()
    global f_num
    global math
    math= "squareN"
    f_num= eval(first_number)
    entry.delete(0,END)
    

def button__log():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END) 
    y= log(f_num)
    entry.insert(0,y)

def button__exp():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END) 
    y= exp(f_num)
    entry.insert(0,y)

def button__factorial():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END) 
    y= factorial(f_num)
    entry.insert(0,y)


def button__inv__sine():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END)
    y=degrees(asin(f_num))
    entry.insert(0,y)

def button__inv__cosine():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END)
    y= degrees(acos(f_num))
    entry.insert(0,y)

def button__inv__tangent():
    first_number= entry.get()
    global f_num
    f_num= eval(first_number)
    entry.delete(0,END)
    y= degrees(atan(f_num))
    entry.insert(0,y)

root= Tk()
root.title('Simple Calculator')
root.iconbitmap("C:\\Users\\USER\\Pictures\\Calculator_Metro.ico")

entry= Entry(font=("Verdana", 18),bg='white', fg='black',width=42)
entry.grid(row=0, column=0, columnspan=5)
space= Label(text="  ")
space.grid(row=1,column=0,rowspan=3)

#define buttons
button_power2= Button(text="x^2",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=32,pady=4,command=button__power2)
button_powerN= Button(text="x^n",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=32,pady=4,command=button__powerN)
button_sin= Button(text="sin(x)",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=24,pady=4,command=button__sine)
button_cos= Button(text="cos(x)",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=24,pady=4,command= button__cosine)
button_tan= Button(text="tan(x)",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=22,pady=4,command= button__tangent)


button_squared= Button(text="x^1/2",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=24,pady=4,command= button__squ_root)
button_10x= Button(text="x^1/n",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=24,pady=4,command=button__sqrtN )
button_log= Button(text="log(n)",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=24,pady=4,command= button__log)
button_exp= Button(text="e",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=41,pady=4,command= button__exp)
button_pi= Button(text="pi",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=38,pady=4,command=lambda: button_click(pi))

button_factorial= Button(text="n!",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=39,pady=4,command= button__factorial)
button_inv_sin= Button(text="sin^-1",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=24,pady=4,command=  button__inv__sine)
button_inv_cos= Button(text="cos^-1",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=24,pady=4,command= button__inv__cosine)
button_inv_tan= Button(text="tan^-1",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=24,pady=4,command= button__inv__tangent)
button_decimal= Button(text=".",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=44,pady=4,command= lambda: button_click("."))

button_1= Button(text="1",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=42,pady=4,command= lambda: button_click(1))
button_2= Button(text="2",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command=  lambda: button_click(2))
button_3= Button(text="3",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command=  lambda: button_click(3))
button_4= Button(text="4",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command=  lambda: button_click(4))
button_5= Button(text="5",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command=  lambda: button_click(5))
button_6= Button(text="6",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command=  lambda: button_click(6))
button_7= Button(text="7",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command=  lambda: button_click(7))
button_8= Button(text="8",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command= lambda: button_click(8))
button_9= Button(text="9",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command= lambda: button_click(9))
button_0= Button(text="0",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command= lambda: button_click(0))
button__add= Button(text="+",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command= button_add)


button__subtract= Button(text="-",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command= button_subtract)
button__multiply= Button(text="x",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command= button_multiply)
button__divide= Button(text="/",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=40,pady=4,command= button_divide)
button__equal= Button(text="=",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=41,pady=4,command=button_equal)
button__clear= Button(text="C",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=106,pady=4,bd=1,relief=SUNKEN,command= button_pop)
button__CE= Button(text="CE",font=("Comic Sans MS", 12),bg='grey', fg='white',padx=98,pady=4,bd=1,relief= SUNKEN,command= button_clear)


#griding button on screen
button_power2.grid(row=5,column=0)
button_powerN.grid(row=5,column=1)
button_sin.grid(row=5,column=2)
button_cos.grid(row=5,column=3)
button_tan.grid(row=5,column=4)

button_squared.grid(row=8,column=0)
button_10x.grid(row=8,column=1)
button_log.grid(row=8,column=2)
button_exp.grid(row=8,column=3)
button_pi.grid(row=8,column=4)

button_inv_cos.grid(row=11, column=0)
button_1.grid(row=11,column=1)
button_2.grid(row=11,column=2)
button_3.grid(row=11,column=3)
button__subtract.grid(row=11, column=4)


button_inv_sin.grid(row=10,column=0)
button_4.grid(row=10,column=1)
button_5.grid(row=10,column=2)
button_6.grid(row=10,column=3)
button__multiply.grid(row=10, column=4)

button_factorial.grid(row=9,column=0)
button__divide.grid(row=9, column=4)
button_7.grid(row=9,column=1)
button_8.grid(row=9,column=2)
button_9.grid(row=9,column=3)


button__equal.grid(row=12, column=3)
button_0.grid(row=12,column=2)
button__add.grid(row=12, column=4)
button_decimal.grid(row=12, column=1)
button_inv_tan.grid(row=12, column=0)

button__clear.grid(row=13, column=0,columnspan=2)
button__CE.grid(row=13, column=3, columnspan=2)
root.protocol('WM_DELETE_WINDOW', quitter_function)

mainloop()
