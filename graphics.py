import tkinter as tk
from tkinter import Tk


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__canves = tk.Canvas(self.__root, width=width, height=height, bg="white")
        self.__canves.pack(fill="both", expand=1)
        self.__is_runnig = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__is_runnig = True
        while self.__is_runnig is True:
            self.redraw()

    def close(self):
        self.__s_runnig = False
