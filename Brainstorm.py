import random
from tkinter import *
from tkinter import messagebox
f = open('nounlist.txt','r');
nounlist = f.readlines()
for i in range(len(nounlist)):
    nounlist[i]=nounlist[i].replace('\n','')
def bs(a):
    w=[]
    strw=''
    for i in range(a):
        w.append(nounlist[random.randint(0,len(nounlist))])
        strw=strw+nounlist[random.randint(0,len(nounlist))]+', '
    strw=strw[:-2]
    msg = messagebox.showinfo('brainstormed',strw)
top = Tk()
L1 = Label(top,text = "number of words")
L1.grid(row = 0)
E1 = Entry(top, bd = 5)
E1.grid(row =0,column = 1)
b = Button(top,text = 'BRAINSTORM',command = lambda: bs(int(E1.get())),bg = 'Blue',fg='White')
b.grid(row =1,columnspan=2)
top.mainloop()
