from draw_lines import Line, Point
from graphics import Window


def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(400, 300)

    line = Line(p1, p2)
    win.draw_line(line, "black")
    win.wait_for_close()


main()
