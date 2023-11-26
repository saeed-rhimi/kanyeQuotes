import requests
from tkinter import *


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfigure(kanye_quote_text, text=quote)


window = Tk()
window.config(padx=30, pady=20)
canvas = Canvas(width=300, height=414)
canvas.pack()
background_image = PhotoImage(file="background.png")
background = canvas.create_image(150, 207, image=background_image)
kanye_quote_text = canvas.create_text(150, 190, text="quote", font=("Ariel", 20, "bold"),
                                      width=250, fill="white")
canvas.grid(row=0, column=0, columnspan=3)

kanye_image = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_image, command=get_quote)
kanye_button.config(highlightthickness=0)
kanye_button.grid(row=1, column=1)

get_quote()

window.mainloop()
