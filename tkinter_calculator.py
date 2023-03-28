from tkinter import *


# Function
def process():
    if entred_process.get() == "+":
        result = float(input1.get()) + float(input2.get())
        result_label.config(text=f"{input1.get()} {entred_process.get()} {input2.get()} = {result}")

    elif entred_process.get() == "-":
        result = float(input1.get()) - float(input2.get())
        result_label.config(text=f"{input1.get()} {entred_process.get()} {input2.get()} = {result}")

    elif entred_process.get() == "x":
        result = float(input1.get()) * float(input2.get())
        result_label.config(text=f"{input1.get()} {entred_process.get()} {input2.get()} = {result}")

    elif entred_process.get() == "/":
        result = float(input1.get()) / float(input2.get())
        result_label.config(text=f"{input1.get()} {entred_process.get()} {input2.get()} = {result}")


# Window
window = Tk()
window.title("Calculator")
window.config(padx=100, pady=100)

# Input
input1 = Entry(width=7)
input1.grid(column=3, row=0)

input2 = Entry(width=7)
input2.grid(column=5, row=0)

entred_process = Entry(width=7)
entred_process.grid(column=4, row=0)

# Button
result_button = Button(text="=", command=process)
result_button.grid(column=3, row=4)

# Label
result_label = Label(text="0")
result_label.grid(column=4, row=4)

num1_label = Label(text="Num1")
num1_label.grid(column=3, row=1)

num2_label = Label(text="Num2")
num2_label.grid(column=5, row=1)

process_label = Label(text="Process (+, -, x, /)")
process_label.grid(column=4, row=1)


window.mainloop()