from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=18, pady=18)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

answer_label = Label()
answer_label.grid(column=1, row=1)

def calculation():
    x =int(miles_input.get())
    y = x * 1.60934
    answer_label.config(text=f"{y}")

button = Button(text="Calculate", command=calculation)
button.grid(column=1, row=2)

window.mainloop()