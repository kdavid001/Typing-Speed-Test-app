from tkinter import *
from tkinter import ttk, messagebox
from faker import Faker
import time
import csv

# TODO: optimize the highscore recording stuff
# Initialize Window
window = Tk()
window.title('Typing Speed Test')
background_color = 'white'

# Variables
High_Score = 0
CPM = 0
WPM = 0
word_array = []
faker = Faker()
start_time = None
leaderboard_file = "leaderboard.txt"
input_entry = None

# Create Canvas
canvas = Canvas(window, width=800, height=450, highlightthickness=0, background=background_color)
canvas.grid(row=0, column=0, columnspan=3)

# Global UI Elements
name_entry = None
submit_button = None
restart_button = None
name_display = None
word_label = None
input_text = None
typed_label = None
timer_label = None
countdown_time = 60  # 60-second test
wpm_display = None
cpm_display = None
accuracy_display = None


def Generate_words():
    """Generate a fresh list of random words."""
    global word_array
    word_array = [faker.word() for _ in range(50)]
    return " ".join(word_array)


def display_text():
    """Display generated words in the label."""
    global word_label
    words = Generate_words()

    if word_label is None:
        word_label = Label(window, text=words, wraplength=500, justify=LEFT, font=("Arial", 16), padx=10, pady=10)
        word_label.grid(row=0, column=0, columnspan=3)
    else:
        word_label.config(text=words)  # Update label text


def track_input(*args):
    """Track user input dynamically."""
    global typed_label, wpm_display, cpm_display, accuracy_display

    typed_text = input_text.get().strip()
    words_typed = typed_text.split()

    correct_words = 0
    for i in range(len(words_typed)):
        if i < len(word_array) and words_typed[i] == word_array[i]:
            correct_words += 1

    correct = correct_words == len(words_typed)
    color = "green" if correct else "red"

    typed_label.config(text=f"Typed: {typed_text}", wraplength=500, fg=color, justify=LEFT, font=("Arial", 16))

    elapsed = max(1, time.time() - start_time)
    live_wpm = round((len(words_typed) / elapsed) * 60)
    live_cpm = round((len(typed_text) / elapsed) * 60)
    accuracy = round((correct_words / len(words_typed)) * 100) if words_typed else 0

    canvas.itemconfig(wpm_display, text=f"WPM: {live_wpm}")
    canvas.itemconfig(cpm_display, text=f"CPM: {live_cpm}")
    canvas.itemconfig(accuracy_display, text=f"Accuracy: {accuracy}%")


def start_timer(time_left):
    """Start countdown timer."""
    global input_text
    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left}s")
        window.after(1000, start_timer, time_left - 1)
    else:
        if input_entry:
            input_entry.config(state=DISABLED)
        calculate_results()


def start_test():
    """Start the typing speed test."""
    global start_time
    start_time = time.time()
    start_timer(countdown_time)


def calculate_results():
    """Calculate WPM, CPM, and Accuracy."""

    end_time = time.time()
    elapsed_time = max(1, end_time - start_time)

    typed_words = input_text.get().split()
    correct_words = 0
    for typed, actual in zip(typed_words, word_array):
        if typed == actual:
            correct_words += 1

    global WPM, CPM
    CPM = round((len(input_text.get()) / elapsed_time) * 60)
    WPM = round((len(typed_words) / elapsed_time) * 60)
    accuracy = round((correct_words / len(typed_words)) * 100) if typed_words else 0

    name = name_entry.get() or "Anonymous"
    save_to_csv(name, WPM, accuracy)

    messagebox.showinfo("Results", f"{name}\nWPM: {WPM}\nCPM: {CPM}\nAccuracy: {accuracy}%")

    input_text.set("")
    typed_label.config(text="Typed: ")


def save_to_csv(name, wpm, accuracy):
    """Save results to CSV."""
    with open(leaderboard_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, wpm, accuracy])


def show_leaderboard():
    """Show saved leaderboard scores."""
    try:
        with open(leaderboard_file, "r") as file:
            reader = csv.reader(file)
            scores = "\n".join([f"{row[0]}: {row[1]} WPM | {row[2]}% Accuracy" for row in reader])
            messagebox.showinfo("Leaderboard", scores)
    except FileNotFoundError:
        messagebox.showinfo("Leaderboard", "No scores yet!")


def start():
    """Initialize the Typing Speed Test UI."""
    global name_entry, submit_button, restart_button, name_display, input_text, typed_label, timer_label
    global wpm_display, cpm_display, accuracy_display, input_box, input_entry



    if typed_label:
        typed_label.destroy()
    if timer_label:
        timer_label.destroy()
    canvas.delete("all")

    name_label = canvas.create_text(150, 20, text="Enter your Name:", fill="black", font=("Arial", 20))
    name_entry = ttk.Entry(window)
    canvas.create_window(350, 20, window=name_entry)

    canvas.create_line(0, 50, 800, 50, fill="black", width=2)
    canvas.create_line(0, 100, 800, 100, fill="black", width=2)
    canvas.create_line(0, 400, 800, 400, fill="black", width=2)

    canvas.create_text(700, 20, text=f"High Score: {High_Score}", fill="black", font=("Arial", 20))

    name_display = canvas.create_text(300, 20, text="", font=("Arial", 20), fill="Blue", anchor="w")

    wpm_display = canvas.create_text(250, 75, text=f"WPM: {WPM}", fill="black", font=("Arial", 20))
    cpm_display = canvas.create_text(150, 75, text=f"CPM: {CPM}", fill="black", font=("Arial", 20))
    accuracy_display = canvas.create_text(380, 75, text="Accuracy: 0%", fill="black", font=("Arial", 20))

    def submit():
        name = name_entry.get()
        if not name:
            canvas.create_text(400, 60, text="Name cannot be empty!", fill="red", font=("Arial", 16))
            return

        canvas.delete(name_label)
        name_entry.destroy()
        submit_button.destroy()

        canvas.itemconfig(name_display, text=f"Name: {name}", fill="black")
        start_test()

    def Restart():
        start()
        display_text()

    submit_button = ttk.Button(window, text="Submit", command=submit)
    canvas.create_window(500, 20, window=submit_button)

    restart_button = ttk.Button(window, text="Restart", command=Restart)
    canvas.create_window(500, 75, window=restart_button)

    leaderboard_button = ttk.Button(window, text="Leaderboard", command=show_leaderboard)
    canvas.create_window(650, 75, window=leaderboard_button)

    canvas.create_text(100, 420, text="Type here:", font=("Arial", 12), fill="black", anchor="w")

    input_text = StringVar()
    input_text.trace_add("write", track_input)

    input_entry = ttk.Entry(window, width=60, textvariable=input_text)
    canvas.create_window(450, 420, window=input_entry)

    typed_label = Label(window, text="Typed: ", font=("Arial", 12), fg="blue")
    typed_label.grid(row=2, column=0, columnspan=3, pady=5, )

    timer_label = Label(window, text="Time Left: 60s", font=("Arial", 14))
    timer_label.grid(row=3, column=0, columnspan=3)

    display_text()


start()
window.mainloop()
