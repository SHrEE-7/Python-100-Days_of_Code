from textwrap import fill
from tkinter import *
from turtle import position 
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("Data/English_Marathi.csv") 
to_learn=data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(2000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Marathi")
    canvas.itemconfig(card_word,text=current_card["Marathi"])
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer=window.after(2000,func=flip_card)


canvas = Canvas(width=800,height=529)
card_front_img = PhotoImage(file="Images/front.png")
card_back_img= PhotoImage(file="Images/back.png")
card_background=canvas.create_image(480,263,image=card_front_img)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"italic"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)

cross_image = PhotoImage(file="Images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="Images/right.png")
unknown_button = Button(image=check_image, highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=1)

next_card()

window.mainloop()  