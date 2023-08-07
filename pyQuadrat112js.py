#!/usr/bin/env python3

import keyboard
from tkinter import *

def draw_rect(canvas, x, y, width, height, outline, fill):
    canvas.create_rectangle(x - 81, y, x + width - 81, y + height, outline=outline, fill=fill, width=1)

# Функция для закрытия окна по нажатию Ctrl+Q
def check_for_quit(root, event):
    if event.keysym.lower() == 'q' and event.state == 0x4:
        root.destroy()

def main():
    root = Tk()
    root.title('Rectangles')

    canvas_width = 671
    canvas_height = 739
    canvas_x_position = 0
    canvas_y_position = 0

    root.geometry(f'{canvas_width}x{canvas_height}+{canvas_x_position}+{canvas_y_position}')

    canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='#150051')
    canvas.pack()

    # Рисуем прямоугольники
    canvas.create_rectangle(56, 37, 306, 287, outline='DarkCyan', fill='Gold', width=1)
    canvas.create_rectangle(406, 387, 616, 597, outline='DarkCyan', fill='Blue', width=1)
    canvas.create_rectangle(221, 412, 406, 597, outline='DarkCyan', fill='SteelBlue', width=1)
    canvas.create_rectangle(306, 37, 481, 212, outline='DarkCyan', fill='DarkOrange', width=1)
    canvas.create_rectangle(56, 432, 221, 597, outline='DarkCyan', fill='MediumOrchid', width=1)
    canvas.create_rectangle(56, 287, 201, 432, outline='DarkCyan', fill='Tomato', width=1)
    canvas.create_rectangle(481, 37, 616, 172, outline='DarkCyan', fill='OrangeRed', width=1)
    canvas.create_rectangle(201, 287, 326, 412, outline='DarkCyan', fill='PaleGreen', width=1)
    canvas.create_rectangle(496, 267, 616, 387, outline='DarkCyan', fill='Red', width=1)
    canvas.create_rectangle(521, 172, 616, 267, outline='DarkCyan', fill='LawnGreen', width=1)
    canvas.create_rectangle(406, 297, 496, 387, outline='DarkCyan', fill='Aquamarine', width=1)
    canvas.create_rectangle(381, 212, 466, 297, outline='DarkCyan', fill='GreenYellow', width=1)
    canvas.create_rectangle(326, 332, 406, 412, outline='DarkCyan', fill='Yellow', width=1)
    canvas.create_rectangle(306, 212, 381, 287, outline='DarkCyan', fill='YellowGreen', width=1)
    canvas.create_rectangle(466, 212, 521, 267, outline='DarkCyan', fill='MediumSeaGreen', width=1)
    canvas.create_rectangle(326, 287, 371, 332, outline='DarkCyan', fill='GreenYellow', width=1)
    canvas.create_rectangle(481, 172, 521, 212, outline='DarkCyan', fill='DarkRed', width=1)
    canvas.create_rectangle(371, 297, 406, 332, outline='DarkCyan', fill='Pink', width=1)
    canvas.create_rectangle(466, 267, 496, 297, outline='DarkCyan', fill='MediumVioletRed', width=1)
    canvas.create_rectangle(201, 412, 221, 432, outline='DarkCyan', fill='LightSeaGreen', width=1)
    canvas.create_rectangle(371, 287, 381, 297, outline='DarkCyan', fill='Cornsilk', width=1)

    root.bind('<Key>', lambda event: check_for_quit(root, event))
    root.mainloop()

if __name__ == '__main__':
    main()
