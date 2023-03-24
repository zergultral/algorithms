"""
from tkinter import *

root = Tk()

c = Canvas(root, width=1000, height=500, bg='white')
c.pack()

c.create

root.mainloop()
"""
from tkinter import *
from random import *

tk = Tk()
c = Canvas(tk, width=1000, height=500, bg='#aaaadd')
c.pack()

while True:
    x, y, size = randint(0, 1000), randint(-100, 0), randint(3, 5)
    c.create_rectangle(x, y, x + size, y + size)
    

mainloop()
