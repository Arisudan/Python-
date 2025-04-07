from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()


top.geometry("200x200")
def show():
   num = askinteger("Input", "Enter no. of years")
   amt = askinteger("Input", "Enter total amount")
   print((amt/(num*12))+0.85*(amt/(num*12)))
   print("AVOID EMI")
   
B = Button(top, text ="EMI for home loan", command = show)
B.place(x=50,y=50)


top.mainloop()
