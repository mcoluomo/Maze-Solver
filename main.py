from tkinter import Tk as tk
from tkinter import Canvas, Pack


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("My Application")
        self.canves = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canves.pack(anchor=self.canves.CENTER, expand=True)
        self.is_runnig = False

    def redraw(self):
        self.update()
        self.update_idletasks()
