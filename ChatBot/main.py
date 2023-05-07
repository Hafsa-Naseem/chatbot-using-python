from tkinter import *
from PIL import ImageTk , Image

tkobj= Tk()

tkobj.title("Pybot")
img = Image.open(r"C:\Users\hp\Downloads\pybot-removebg-preview.png")
img = ImageTk.PhotoImage(img)
tkobj.iconphoto(False,img)
tkobj.configure(bg='skyblue')
img1=Image.open(r"C:\Users\hp\Downloads\pybot-removebg-preview.png")

img1=img1.resize((25,25))
img1 = ImageTk.PhotoImage(img1)
intro_msg=Label(tkobj,text="    Hi my name is Pybot. I hope that you're doing fine."
                           " Feel free to ask me anything \n related to Python and"
                           " I'll do my best to help you out!",image=img1,compound='left',bg='skyblue')
intro_msg.grid(row=0,column=0)

def b1body(img1=img1):
  l1=Label(tkobj,text="Python is a high-level, general-purpose programming language.",
           border=10,background='blue',compound='right')
  l1.grid(row=5,column=1)
b1= Button(tkobj,text= "What is python",font= ("Arial",9),command=b1body,background='navy blue')
b1.grid()

def b2body(img1=img1):
  l2=Label(tkobj,text="A function is a block of code  which only runs when it is called.", border=10,background='blue',compound='right')
  l2.grid(row=7,column=1)
b2= Button(tkobj,text= "What is a function in python",font= ("Arial",9),command=b2body,background='navy blue',compound='right')
b2.grid()

def b3body(img1=img1):
  l3=Label(tkobj,text="Variable is container for storing data values.", border=10,background='blue',compound='right')
  l3.grid(row=9,column=1)
b3= Button(tkobj,text=  "What is a variable",font= ("Arial",9),command=b3body,background='navy blue',compound='right')
b3.grid()

def b4body(img1=img1):
  l4=Label(tkobj,text="A dictionary is a collection which is ordered, changeable and \ndo not allow duplicates and used to store values in key,value pair.", border=10,background='blue',compound='right')
  l4.grid(row=11,column=1)
b4= Button(tkobj,text=  "What is a dictionary in python",font= ("Arial",9),command=b4body,background='navy blue',compound='right')
b4.grid()

def b5body(img1=img1):
  l5=Label(tkobj,text="Lists are used to store multiple items in a single variable.", border=10,background='blue',compound='right')
  l5.grid(row=13,column=1)
b5= Button(tkobj,text=  "What is a list in python",font= ("Arial",9),command=b5body,background='navy blue',compound='right')
b5.grid()


tkobj.mainloop()


