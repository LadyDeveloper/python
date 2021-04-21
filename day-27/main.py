#%%
from tkinter import *

#Change the label text to the string inside input
def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("My first GUI Python!!")
window.minsize(width=500, height=300)
#Changing the padding
window.config(padx=20, pady=20)


#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.pack(expand="true")
#my_label["text"] = "My text"
my_label.config(text="My text")
my_label.grid(column=0, row=0)

#Button
#In order to use the function button_clicked command is necessary
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


#Button 2
button2 = Button(text="New button")
button2.grid(column=2, row=0)

#Entry
input = Entry(width=20)
print(input.get())
input.grid(column=3, row=2)




window.mainloop()
# %%
