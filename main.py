from tkinter import *
from tkinter import ttk
from PIL import ImageFont, ImageDraw, Image
import matplotlib.pyplot as plt
import datetime as dt

window = Tk()
window.title('Typing Speed Test')
background_color = 'white'
background_image = PhotoImage(file="card_front.png")
High_Score = 0
CPM = 5
WPM = CPM * 5

canvas = Canvas(window, width=800, height=450, highlightthickness=0, background=background_color)
canvas.grid(row=0, column=0, columnspan=3)



def start(WPM, CPM, High_Score):
    # Name Input Field
    name_label = canvas.create_text(150, 20, text="Enter your Name:", fill="black", font=("Arial", 20))
    name_entry = ttk.Entry(window)
    canvas.create_window(350, 20, window=name_entry)

    # Separator Lines
    canvas.create_line(0, 50, 800, 50, fill="black", width=2)
    canvas.create_line(0, 100, 800, 100, fill="black", width=2)

    # High Score Display
    high_score_text = canvas.create_text(700, 20, text=f"High Score: {High_Score}", fill="black", font=("Arial", 20))

    # Placeholder for entered name
    name_display = canvas.create_text(300, 20, text="", font=("Arial", 20), fill="Blue", anchor="w")
    cpm_text = canvas.create_text(150, 75, text=f"CPM: {CPM}", fill="black", font=("Arial", 20))
    wpm_text = canvas.create_text(300, 75, text=f"WPM: {WPM}", fill="black", font=("Arial", 20))


    def submit():
        name = name_entry.get()
        if name == "":
            canvas.create_text(text="name cannot be empty", fill="black", font=("Arial", 20))

        # Remove input field and label
        canvas.delete(name_label)  # Removes "Enter your Name:"
        name_entry.destroy()  # Removes input box
        submit_button.destroy()

        # Update canvas text with entered name
        canvas.itemconfig(name_display, text=f"Name: {name}",fill="black", font=("Arial", 20))


    def Restart():
        start(CPM, WPM, High_Score)


    # Submit Button
    submit_button = ttk.Button(window, text="Submit", command=submit)
    canvas.create_window(500, 20, window=submit_button)

    # Restart_Button
    restart_button = ttk.Button(window, text="Restart", command=Restart)
    canvas.create_window(500, 75, window=restart_button)

start(CPM, WPM, High_Score)
window.mainloop()