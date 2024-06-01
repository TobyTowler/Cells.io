from tkinter import Tk, Canvas
import game
import food

root = Tk()
root.title("Cells.io")
canvas = Canvas(root, width=550, height=550)


def drawFrame():
    drawRectangle()
    # root.mainloop()
    root.after(
        1000,
    )


def drawRectangle():
    canvas.pack()
    canvas.create_oval(5, 5, 10, 10, fill="red")
    root.geometry("400x250+300+300")


def drawFood(x0, x1):
    canvas.pack()
    canvas.create_oval(x0, x1, x0 + 15, x1 + 15, fill="red")
