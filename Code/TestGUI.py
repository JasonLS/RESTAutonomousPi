from tkinter import *
from Motors import *
from Servo import *
Turn_Value = 2 
master = Tk()

Turn_Value = 2 
def callback():
    print ("click!")

f = Button(master, text="Forward", command=forward, height=10, width=10, compound=LEFT)
f.place(x = 150, y = 0)

b = Button(master, text="Backward", command=backward, height=10, width=10)
b.place(x = 150, y = 200)

l = Button(master, text="Left", command=turn_left, height=10, width=10, compound=LEFT)
l.place(x = 50, y = 100)

r = Button(master, text="Right", command=turn_right, height=10, width=10)
r.place(x = 250, y = 100)

c = Button(master, text="Center", command=center, height=10, width=10)
c.place(x = 150, y = 100)

s = Button(master, text="Still", command=still, height=5, width=5)
s.place(x = 300, y = 0)

mainloop()
