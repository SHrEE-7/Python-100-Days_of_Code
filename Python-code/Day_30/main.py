from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import json
from turtle import width
# from pyperclip import copy
#--------------------------- PASSWORD GENERATOR --------------------#
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '9', '8', '7', '6', '5', '4', '3', '2', '1']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    # copy(password)
#--------------------------- SAVE PASSWORD -------------------------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()   
    
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }  

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message= "please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:                
                website_entry.delete(0,END)
                password_entry.delete(0,END) 

#--------------------------- Find Password ------------------------------#
def find_password():
    wesite = website_entry.get()


#--------------------------- UI SETUP ------------------------------#

window = Tk()
window.title("Passwork Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=300, width=220)
logo_img = PhotoImage(file="image.png")
canvas.create_image(100,150,image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website :")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username :")
email_label.grid(column=0,row=2)
password_label = Label(text="Password :")
password_label.grid(column=0,row=3) 


#Eneties
website_entry = Entry(width=30)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry = Entry(width=30)
email_entry.grid(column=1,row=2)
email_entry.insert(0,"e.g. shree@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(column=1,row=3)

#Buttons
search_button=Button(text="search",width=20,command=find_password)
search_button.grid(row=1,column=2)
generate_password_button = Button(text="Generate Passsword",command=generate_password,width=20)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="ADD",width=30,command=save)
add_button.grid(row=5,column=1)



window.mainloop()