from Tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()

def random_rectangle(x, y, z, a, b, c, d, e):
    x1 = random.randrange(x)
    y1 = random.randrange(y)
    x2 = x1 + random.randrange(x)
    y2 = y1 + random.randrange(y)
    x3 = x2 + random.randrange(x)
    y3 = y2 + random.randrange(y)
    z1 = random.randrange(z)
    a1 = random.randrange(a)
    b1 = random.randrange(b)
    c1 = random.randrange(c)
    d1 = random.randrange(d)
    e1 = random.randrange(e)

    color = '#%x%x%x%x%x%x' % (z1, a1, b1, c1, d1, e1)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color, outline="black")

for x in range(0, 200):
    random_rectangle(300, 300, 15, 15, 15, 15, 15, 15)
