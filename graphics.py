from tkinter import Canvas, Tk

from draw_lines import Line


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__canves = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canves.pack(fill="both", expand=1)
        self.__is_runnig = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_runnig = True
        while self.__is_runnig is True:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__is_runnig = False

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canves, fill_color)
