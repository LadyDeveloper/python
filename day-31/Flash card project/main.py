from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = ''
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    dictionary = original_data.to_dict(orient="records")
else:
    dictionary = data.to_dict(orient="records")

#-----------Create new flash cards------------------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dictionary)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

#-------------------Flip Card------------------------------------
def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
 

#-------------------Remove Card------------------------------------
def remove_card():
    dictionary.remove(current_card)
    data = pandas.DataFrame(dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


#-------------------User Interface------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img,  highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img,  highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()



window.mainloop()

