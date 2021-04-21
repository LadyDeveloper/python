from tkinter import *

def calculate():
    result_km = round(float(input_entry.get()) * 1.609344)
    label_result.config(text=result_km)

#Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=40, pady=40)

input_entry = Entry(width=10)
input_entry.insert(END, string="0")
input_entry.grid(column=1, row=0)


#Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)
label_miles.config(padx=20, pady=10)

label_info = Label(text="is equal to")
label_info.grid(column=0, row=1)
label_info.config(padx=0, pady=10)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

#Button

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()