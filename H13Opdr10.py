from tkinter import *
import math

tk = Tk()


class Ster:

    def __init__(self):
        self.canvas = Canvas(tk, width=1000, height=1000, bg="white")

        self.canvas.pack()
        self.tekenSter()

        mainloop()

    def tekenSter(self):
        x_c = 500
        y_c = 500
        R = 100

        r = R * (1 - math.cos(2 * math.pi / 5)) * math.tan(2 * math.pi / 5)
        vertices = [
            x_c + R * math.sin(2 * math.pi / 5),
            y_c + R * math.cos(2 * math.pi / 5),

            x_c + r * math.sin(math.pi / 5),
            y_c + r * math.cos(math.pi / 5),

            x_c,
            y_c + R,

            x_c - r * math.sin(math.pi / 5),
            y_c + r * math.cos(math.pi / 5),

            x_c - R * math.sin(2 * math.pi / 5),
            y_c + R * math.cos(2 * math.pi / 5),

            x_c - r * math.sin(2 * math.pi / 5),
            y_c - r * math.cos(2 * math.pi / 5),

            x_c - R * math.sin(math.pi / 5),
            y_c - R * math.cos(math.pi / 5),

            x_c,
            y_c - r,

            x_c + R * math.sin(math.pi / 5),
            y_c - R * math.cos(math.pi / 5),

            x_c + r * math.sin(2 * math.pi / 5),
            y_c - r * math.cos(2 * math.pi / 5),
        ]

        self.canvas.create_polygon(
            vertices,
            fill='white',
            outline='black'
        )

        self.canvas.create_text(
            x_c,
            y_c,
            text="Luc Hengeveld"
        )


def main():
    Ster()


main()
