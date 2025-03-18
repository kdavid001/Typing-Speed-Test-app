from tkinter import *
from tkinter import ttk
from random_word import RandomWords

window = Tk()
window.title('Typing Speed Test')
background_color = 'white'

# Variables
High_Score = 0
CPM = 5
WPM = CPM * 5

# Create Canvas
canvas = Canvas(window, width=800, height=450, highlightthickness=0, background=background_color)
canvas.grid(row=0, column=0, columnspan=3)

# Global Variables
name_entry = None
submit_button = None
restart_button = None
name_display = None
word_array = []
random_words = RandomWords()

for n in range(1, 100):
    word = random_words.get_random_word()
    word_array.append(random_words)




def start():
    global name_entry, submit_button, restart_button, name_display

    # Clear previous elements
    canvas.delete("all")

    # Name Input Field
    name_label = canvas.create_text(150, 20, text="Enter your Name:", fill="black", font=("Arial", 20))
    name_entry = ttk.Entry(window)
    canvas.create_window(350, 20, window=name_entry)

    # Separator Lines
    canvas.create_line(0, 50, 800, 50, fill="black", width=2)
    canvas.create_line(0, 100, 800, 100, fill="black", width=2)
    canvas.create_line(0, 400, 800, 400, fill="black", width=2)

    # High Score Display
    high_score_text = canvas.create_text(700, 20, text=f"High Score: {High_Score}", fill="black", font=("Arial", 20))

    # Placeholder for entered name
    name_display = canvas.create_text(300, 20, text="", font=("Arial", 20), fill="Blue", anchor="w")
    cpm_text = canvas.create_text(150, 75, text=f"CPM: {CPM}", fill="black", font=("Arial", 20))
    wpm_text = canvas.create_text(300, 75, text=f"WPM: {WPM}", fill="black", font=("Arial", 20))

    # Function to handle name submission
    def submit():
        name = name_entry.get()
        if not name:
            canvas.create_text(400, 60, text="Name cannot be empty!", fill="red", font=("Arial", 16))
            return

        # Remove input field and label
        canvas.delete(name_label)
        name_entry.destroy()
        submit_button.destroy()

        # Update name display
        canvas.itemconfig(name_display, text=f"Name: {name}", fill="black")

    # Restart function
    def Restart():
        start()

    # Submit Button
    submit_button = ttk.Button(window, text="Submit", command=submit)
    canvas.create_window(500, 20, window=submit_button)

    # Restart Button
    restart_button = ttk.Button(window, text="Restart", command=Restart)
    canvas.create_window(500, 75, window=restart_button)

    # Typing Section
    canvas.create_text(100, 420, text="Type here:", font=("Arial", 12), fill="black", anchor="w")
    type_section = ttk.Entry(window, width=60)
    canvas.create_window(450, 420, window=type_section)

    def display_text():
        # Create a Text widget

        window.title("Wrapped Text Example")

        long_text = """This is an example of a long text that needs to be wrapped automatically within a specific space.
        It will be displayed in a label with proper indentation and alignment."""

        # Label with text wrapping
        label = Label(window, text=long_text, wraplength=500, justify=LEFT, font=("Arial", 14), padx=20, pady=20)
        label.pack()

        window.mainloop()
    display_text()
# Start the app
start()
window.mainloop()