from asyncore import read
from audioop import cross
from cgitb import text
from tkinter import *
from turtle import position 
import pandas
import random

data = pandas.read_csv("Data/English_Marathi.csv") 
to_learn=data.to_dict(orient="records")


BACKGROUND_COLOR = "#B1DDC6"

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])
window = Tk()
window.title("Flashy")

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=529)
card_front_img = PhotoImage(file="Images/front.png")
canvas.create_image(480,263,image=card_front_img)
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