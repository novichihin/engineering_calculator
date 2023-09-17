from tkinter import *
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_equal():
    current = entry.get()
    entry.delete(0, END)
    try:
        result = eval(current)
        entry.insert(0, result)
    except:
        entry.insert(0, "Ошибка")

def button_clear():
    entry.delete(0, END)

def button_sin():
    current = entry.get()
    entry.delete(0, END)
    try:
        result = math.sin(math.radians(eval(current)))
        entry.insert(0, result)
    except:
        entry.insert(0, "Ошибка")

def button_cos():
    current = entry.get()
    entry.delete(0, END)
    try:
        result = math.cos(math.radians(eval(current)))
        entry.insert(0, result)
    except:
        entry.insert(0, "Ошибка")

def button_tan():
    current = entry.get()
    entry.delete(0, END)
    try:
        result = math.tan(math.radians(eval(current)))
        entry.insert(0, result)
    except:
        entry.insert(0, "Ошибка")

window = Tk()
window.title("Инженерный калькулятор")


entry = Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = Button(window, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=30, pady=20, command=lambda: button_click(0))


button_add = Button(window, text="+", padx=30, pady=20, command=lambda: button_click("+"))
button_subtract = Button(window, text="-", padx=30, pady=20, command=lambda: button_click("-"))
button_multiply = Button(window, text="*", padx=30, pady=20, command=lambda: button_click("*"))
button_divide = Button(window, text="/", padx=30, pady=20, command=lambda: button_click("/"))
button_equal = Button(window, text="=", padx=30, pady=20, command=button_equal)
button_clear = Button(window, text="C", padx=30, pady=20, command=button_clear)
button_sin = Button(window, text="sin", padx=20, pady=20, command=button_sin)
button_cos = Button(window, text="cos", padx=20, pady=20, command=button_cos)
button_tan = Button(window, text="tan", padx=20, pady=20, command=button_tan)


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)
button_sin.grid(row=1, column=4)
button_cos.grid(row=2, column=4)
button_tan.grid(row=3, column=4)

window.mainloop()