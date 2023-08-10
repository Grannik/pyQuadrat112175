#!/usr/bin/env python3

from tkinter import *

def close_window(root):
    root.destroy()

def main():
    root = Tk()
    root.title('Clock')
    root.overrideredirect(1)  # Убираем рамку окна (без рамки)
    root.geometry('336x364+120+50')  # Размер окна и его положение

    canvas = Canvas(root, width=336, height=336, bg='black')
    canvas.pack()

    # Квадраты. Всё на три умножать.
    canvas.create_rectangle(0, 0, 150, 150, fill='#FDE200')     #q50
    canvas.create_rectangle(210, 210, 336, 336, fill='#0000FF') #q42
    canvas.create_rectangle(99, 225, 210, 336, fill='#B5ADCF')  #q37
    canvas.create_rectangle(150, 0, 255, 105, fill='#FDAD00')   #q35
    canvas.create_rectangle(0, 237, 99, 336, fill='#FDADCF')    #q33
    canvas.create_rectangle(0, 150, 87, 237, fill='#FF7F52')    #q29
    canvas.create_rectangle(255, 0, 336, 81, fill='#FD6E00')    #q27
    canvas.create_rectangle(87, 150, 162, 225, fill='#9EFF7D')  #q25
    canvas.create_rectangle(264, 138, 336, 210, fill='#FF0000') #q24
    canvas.create_rectangle(279, 81, 336, 138, fill='#D4FF00')  #q19
    canvas.create_rectangle(210, 156, 264, 210, fill='#85FFC2') #q18
    canvas.create_rectangle(195, 105, 246, 156, fill='#85FF00') #q17
    canvas.create_rectangle(162, 177, 210, 225, fill='#FFFF24') #q16
    canvas.create_rectangle(150, 105, 195, 150, fill='#C4CC00') #q15
    canvas.create_rectangle(246, 105, 279, 138, fill='#D400FF') #q11
    canvas.create_rectangle(162, 150, 189, 177, fill='#EBFF00') #q9
    canvas.create_rectangle(255, 81, 279, 105, fill='#DE0000')  #q8
    canvas.create_rectangle(189, 156, 210, 177, fill='#FF46FF') #q7
    canvas.create_rectangle(246, 138, 264, 156, fill='#9E3D45') #q6
    canvas.create_rectangle(87, 225, 99, 237, fill='#0073FF')   #q4
    canvas.create_rectangle(189, 150, 195, 156, fill='#FFFFD0') #q2

    # Добавляем узкую кнопку закрытия программы
    close_button = Button(root, text="Close program", command=lambda: close_window(root), font=('Arial', 8) ,width=51, height=1)
    close_button.place(x=0, y=336) # положение кнопки

    root.mainloop()

if __name__ == '__main__':
    main()

