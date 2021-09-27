from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=240)
window.config(padx=10, pady=20)

input = Entry(width=7)
input.get()
input.grid(column=1, row=0)

label_input = Label(text="Miles")
label_input.grid(column=2, row=0)

label_part1 = Label(text="is equal to ")
label_part1.grid(column=0, row=1)

label_part2 = Label(text="0")
label_part2.grid(column=1, row=1)

label_part3 = Label(text=" Km")
label_part3.grid(column=2, row=1)


def convert_formula():
    the_km = round(int(input.get()) * 1.609, 2)
    label_part2["text"] = f"{the_km}"


button = Button(text="Calculate", command=convert_formula)
button.grid(column=1, row=2)

window.mainloop()
