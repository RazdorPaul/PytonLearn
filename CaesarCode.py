import tkinter as tk
from tkinter import *
import funtionsCaesar as fc


def left():
    global shift
    shift = 1
    str_shift.set("Выбран левый сдвиг")

def right():
    global shift
    shift = 2
    str_shift.set("Выбран правый сдвиг")

def crypt():
    str_shift.set('')
    str_text.set('')
    buff_str = text.get(0.0, END)
    buff_key = entry_key.get()
    if buff_key == '':
        str_text.set("Введите число для шифрования!")
        return
    if shift == 0:
        str_shift.set("Введите направление сдвига!")
        return
    if buff_str.isspace() == True:
        str_text.set("Введите текст для шифрования!")
        return
    buff_str = fc.caesarCrypt(buff_str, buff_key, shift)
    text.delete(0.0, END)
    text.insert(1.0, buff_str)
    str_shift.set("Ваш текст зашифрован")
    str_text.set("Для дешифровки поменяйте направление сдвига")

def checking(num):
    return num == '' or num.isnumeric()


shift = 0
frame = tk.Tk()
frame.title("Шифр Цезаря")
frame.geometry("400x250")
frame.resizable(False, False)

str_text = StringVar()
str_shift = StringVar()
lab_key = tk.Label(frame, text = "В поле ниже укажите ключ")
lab_key.grid(row=2, column=1)
lab_text = tk.Label(frame, text = "В поле ниже введите шифруемый текст")
lab_text.grid(row=0, column=0, columnspan=3)
err_shift = tk.Label(frame, textvariable = str_shift)
err_shift.grid(row=6, column=0, columnspan=3)
err_text = tk.Label(frame, textvariable = str_text)
err_text.grid(row=7, column=0, columnspan=3)

text = tk.Text(frame, width=50, height=7, wrap=WORD)
text.grid(row=1, column=0, columnspan=3)

check = (frame.register(checking), "%P")
entry_key = tk.Entry(frame, width=24, validate="key", validatecommand=check)
entry_key.grid(row=4, column=1)

r_shift = tk.Button(frame, text="сдвиг вправо", width=15, command=right)
r_shift.grid(row=4, column=2)
l_shift = tk.Button(frame, text="сдвиг влево", width=15, command=left)
l_shift.grid(row=4, column=0)
crypto = tk.Button(frame, text="зашифровать", width=17, command=crypt)
crypto.grid(row=5, column=1)
frame.mainloop()


