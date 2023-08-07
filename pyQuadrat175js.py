#!/usr/bin/env python3

from tkinter import *

def draw_rect(canvas, x, y, width, height, outline, fill):
    canvas.create_rectangle(x, y, x + width, y + height, outline=outline, fill=fill, width=1)

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

    # Задание значения переменной
    shift_amount = 235

    # Рисуем прямоугольники
    draw_rect(canvas, 530 - shift_amount, 210, 3, 3, 'black', 'Lavender')
    draw_rect(canvas, 593 - shift_amount, 474, 6, 6, 'black', 'Purple')
    draw_rect(canvas, 521 - shift_amount, 210, 9, 9, 'black', 'Indigo')
    draw_rect(canvas, 521 - shift_amount, 198, 12, 12, 'black', 'Cornsilk')
    draw_rect(canvas, 533 - shift_amount, 198, 15, 15, 'black', 'LightSeaGreen')
    draw_rect(canvas, 680 - shift_amount, 450, 24, 24, 'black', 'MediumVioletRed')
    draw_rect(canvas, 521 - shift_amount, 171, 27, 27, 'black', 'Pink')
    draw_rect(canvas, 548 - shift_amount, 171, 42, 42, 'black', 'FireBrick')
    draw_rect(canvas, 473 - shift_amount, 171, 48, 48, 'black', 'GreenYellow')
    draw_rect(canvas, 476 - shift_amount, 219, 54, 54, 'black', 'MediumSeaGreen')
    draw_rect(canvas, 530 - shift_amount, 213, 60, 60, 'black', 'YellowGreen')
    draw_rect(canvas, 593 - shift_amount, 387, 87, 87, 'black', 'Yellow')
    draw_rect(canvas, 590 - shift_amount, 297, 90, 90, 'black', 'GreenYellow')
    draw_rect(canvas, 500 - shift_amount, 387, 93, 93, 'black', 'Aquamarine')
    draw_rect(canvas, 500 - shift_amount, 480, 99, 99, 'black', 'LawnGreen')
    draw_rect(canvas, 599 - shift_amount, 474, 105, 105, 'black', 'Red')
    draw_rect(canvas, 476 - shift_amount, 273, 114, 114, 'black', 'PaleGreen')
    draw_rect(canvas, 473 - shift_amount, 54, 117, 117, 'black', 'OrangeRed')
    draw_rect(canvas, 704 - shift_amount, 450, 129, 129, 'black', 'Tomato')
    draw_rect(canvas, 680 - shift_amount, 297, 153, 153, 'black', 'MediumOrchid')
    draw_rect(canvas, 308 - shift_amount, 54, 165, 165, 'black', 'DarkOrange')
    draw_rect(canvas, 308 - shift_amount, 219, 168, 168, 'black', 'SteelBlue')
    draw_rect(canvas, 308 - shift_amount, 387, 192, 192, 'black', 'Blue')
    draw_rect(canvas, 590 - shift_amount, 54, 243, 243, 'black', 'Gold')

    root.bind('<Key>', lambda event: check_for_quit(root, event))
    root.mainloop()

if __name__ == '__main__':
    main()
