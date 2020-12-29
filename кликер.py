from tkinter import *
 
tk = Tk()
 
btn = Button(text='Click',
             width=15,
             height=7)
btn.pack()
 
n = 0


def click(event):
    global n
    n = n + 1
    label['text'] = str(n)
 
btn.bind_all('<Button-1>', click)
 
label = Label(tk,
              text=str(n))
label.pack()