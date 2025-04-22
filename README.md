# 🧠 Typing Speed Test

A simple yet engaging Typing Speed Test desktop application built with Python's Tkinter GUI library. This app helps you measure how fast and accurately you type within a 60-second time frame.

## 🚀 Features

- ⌨️ Random word generation using the `Faker` library
- ⏱️ Live WPM (Words Per Minute), CPM (Characters Per Minute), and Accuracy tracking
- 🧠 Real-time feedback on typed text (correct/incorrect)
- 📊 Leaderboard with CSV-based persistence of top scores
- 🔄 Restart function for unlimited practice sessions
- 👤 Name input and anonymous mode support

## 🛠️ Technologies Used

- Python 3.12+
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI
- [Faker](https://pypi.org/project/Faker/) for random word generation
- CSV for leaderboard data storage

## 🖥️ How It Works

1. Launch the application.
2. Enter your name and click **Submit**.
3. A set of random words will appear.
4. Start typing in the input field below.
5. The timer begins and runs for 60 seconds.
6. Your score is shown after time's up, and your results are saved in `leaderboard.txt`.

## 📂 File Structure

```bash
Typing-Speed-Test/
├── main.py           # Main application logic
├── leaderboard.txt   # Stores the leaderboard data (auto-generated)
└── README.md         # Project documentation
```
📸 VIDEO


https://github.com/user-attachments/assets/0892d95d-89c3-4659-8f06-dc848528c365


📝 Usage

To run the project:
	1.	Clone this repo:

git clone https://github.com/yourusername/typing-speed-test.git
cd typing-speed-test


	2.	Install required dependencies:

pip install faker


	3.	Run the app:

python main.py



✅ To-Do
	<li>Optimize high score detection and display
	<li>Add difficulty levels or themes
 <li>Support for saving and showing only top 5 scores

📬 Contact

Feel free to reach out if you’d like to contribute or suggest improvements.
	<li>Name: David Ogunmola
	<li>Email: korededavid03@gmail.com 
	<li>GitHub: kdavid001
