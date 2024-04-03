import requests
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


# Define the function that get a random joke form the API and displays in the label widget


def get_joke():
    # make an HTTP GET request to the API
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    # Get the JSON data from the response and extract the setup and punchline fields
    data = response.json()
    setup = data["setup"]
    punchline = data["punchline"]

    # Set the text of the label widget to the joke
    joke_label.configure(text=f"{setup}\n\n{punchline}")


# Create the GUI Window

window = tk.Tk()
window.title("Random Joke Generator")
window.geometry("800x500")
style = Style(theme="flatly")
window.style = style

# Create Label Widget

joke_label = tk.Label(text="Click the button to get a random Joke!",
                      font=("TkdefaultFont", 20))

joke_label.place(relx=0.5, rely=0.5, anchor="center")

# create "Get Joke Button" widget

get_joke_button = ttk.Button(text="Get Joke", command=get_joke)
get_joke_button.pack(pady=20)

window.mainloop()
