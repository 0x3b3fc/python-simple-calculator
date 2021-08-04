from tkinter import *

top = Tk()
top.title('calculator')
top.minsize(500, 300)
num1_label = Label(text="First Number")
num1_label.pack()
num1_tb = Entry()
num1_tb.pack()

num2_label = Label(text="Second Number")
num2_label.pack()
num2_tb = Entry()
num2_tb.pack()


def add_num():
    num1 = int(num1_tb.get())
    num2 = int(num2_tb.get())
    res = num1 + num2
    result_label = Label(text=f"Result is: {str(res)}")
    result_label.pack()


def tarh_num():
    num1 = int(num1_tb.get())
    num2 = int(num2_tb.get())
    res = num1 - num2
    result_label = Label(text=f"Result is: {str(res)}")
    result_label.pack()


def darb_num():
    num1 = int(num1_tb.get())
    num2 = int(num2_tb.get())
    res = num1 * num2
    result_label = Label(text=f"Result is: {str(res)}")
    result_label.pack()


def esma_num():
    num1 = int(num1_tb.get())
    num2 = int(num2_tb.get())
    res = num1 / num2
    result_label = Label(text=f"Result is: {str(res)}")
    result_label.pack()


but_add = Button(text="summation", command=add_num)
but_add.pack()

but_tarh = Button(text="subtraction", command=tarh_num)
but_tarh.pack()

but_darb = Button(text="Multiplication", command=darb_num)
but_darb.pack()

but_esma = Button(text="Division", command=esma_num)
but_esma.pack()

top.mainloop()
