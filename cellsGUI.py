from tkinter import Tk, Canvas

root = Tk()
root.title("Cells.io")


def drawFrame():
    drawRectangle()
    root.mainloop()


def drawRectangle():
    canvas = Canvas(root, width=550, height=820)
    canvas.pack()
    canvas.create_rectangle(50, 0, 100, 50, fill="red")
    root.geometry("400x250+300+300")
