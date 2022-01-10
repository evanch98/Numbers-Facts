from tkinter import (
    Tk,
    PhotoImage,
    Label,
    Button,
    Canvas,
    messagebox
)
import requests
import webbrowser
import pyperclip
import os

BG_COLOR = "#CEE5D0"
TEXT_COLOR = "#FFBF86"
FONT = ("Forte", 20)
ATTRIBUTION = "The facts are from Numbers API"
OWNER = os.environ.get("OWNER")
facts = ""


# Callback Function
def callback(url):
    webbrowser.open(url)


# Button Functions
def next_facts():
    global facts
    response = requests.get("http://numbersapi.com/random")
    facts = response.text
    canvas.itemconfig(facts_text, text=facts)


def copy():
    pyperclip.copy(facts)
    messagebox.showinfo(title="Info", message="Text copied to the clipboard.")


# UI Setup
root = Tk()
root.title("Numbers' Facts")
root.config(bg=BG_COLOR, padx=10, pady=10)
root.geometry("273x410")
root.resizable(False, False)
root.iconbitmap("./logo.ico")

card_ui = PhotoImage(file="./ui_images/card_ui.png")
next_button_img = PhotoImage(file="./ui_images/next_button.png")
copy_button_img = PhotoImage(file="./ui_images/copy_button.png")

title_label = Label(root, text="Numbers' Facts", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
title_label.grid(row=0, column=0, columnspan=2, pady=20)

canvas = Canvas(root, width=242, height=147, highlightthickness=0, bg=BG_COLOR)
canvas.create_image(121, 74, image=card_ui)
facts_text = canvas.create_text(121, 74, text="Click the next button to start!", width=230, font=("Forte", 12), fill=TEXT_COLOR)
canvas.grid(row=1, column=0, columnspan=3)

next_button = Button(root, image=next_button_img, relief="flat", highlightthickness=0, bg=BG_COLOR, command=next_facts)
next_button.grid(row=2, column=0, padx=7, pady=30)

copy_button = Button(root, image=copy_button_img, relief="flat", highlightthickness=0, bg=BG_COLOR, command=copy)
copy_button.grid(row=2, column=1, padx=7, pady=30)

attr_label = Label(root, text=f"{ATTRIBUTION}, and \n{OWNER}", fg=TEXT_COLOR, bg=BG_COLOR, font=("Forte", 10))
attr_label.grid(row=3, column=0, columnspan=2)

attr_link = Label(root, text="numbersapi.com", fg=TEXT_COLOR, bg=BG_COLOR, cursor="hand2")
attr_link.grid(row=4, column=0, columnspan=2)
attr_link.bind("<Button-1>", lambda e: callback("numbersapi.com"))

root.mainloop()
