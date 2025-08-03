from tkinter import Canvas, Tk

from draw_lines import Line, Point


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


class Cell:
    def __init__(self, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True

        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1
        self.__x2 = -1

        self.__y1 = -1
        self.__y2 = -1
        self.__win = win

    def draw(self, x1, x2, y1, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall is True:
            p1 = Point(x1, x2)
            p2 = Point(y1, y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

        if self.has_top_wall is True:
            p1 = Point(x1, x2)
            p2 = Point(y1, y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

        if self.has_right_wall is True:
            p1 = Point(x1, x2)
            p2 = Point(y1, y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

        if self.has_top_wall is True:
            p1 = Point(x1, x2)
            p2 = Point(y1, y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.__win.draw_line(line, fill_color)
