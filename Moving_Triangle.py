import time
from Tkinter import*
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
myTriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)

for x in range(0, 59):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.05)
for x in range(0, 59):
    canvas.move(1, 0, 5)
    tk.update()
    time.sleep(0.05)
for x in range(0, 59):
    canvas.move(1, -5, 0)
    tk.update()
    time.sleep(0.05)
for x in range(0, 59):
    canvas.move(1, 0, -5)
    tk.update()
    time.sleep(0.05)