# 🎮 Hangman Game

A simple text-based Hangman game built in Python as part of the **CodeAlpha Python Programming Internship**.

## 📌 About

This is a console-based Hangman game where the player guesses a hidden word one letter at a time. The game randomly selects a word from a predefined list and allows a maximum of 6 incorrect guesses before the game ends.

## ⚙️ How It Works

- The program randomly picks a word from a list of 5 predefined words.
- The player guesses one letter at a time.
- Correct guesses reveal the letter's position in the word.
- Incorrect guesses reduce the number of remaining attempts.
- The game ends when the player either guesses the full word (win) or runs out of attempts (lose).

## 🧠 Key Concepts Used

- `random` module
- `while` loops
- `if-else` conditionals
- String manipulation
- Lists and sets

## ▶️ How to Run

1. Make sure Python is installed on your system.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the following command:

​```
python HangmanGame.py
​````
5. Follow the on-screen prompts to guess letters and try to win the game!

## 🎯 Sample Gameplay 
```
Welcome to Hangman! Guess the word.

Word: ______
Attempts left: 6
Guess a letter: p

Word: p_____
Attempts left: 6
Guess a letter: y
```

## 🏆 Internship

This project was completed as **Task 1** of the Python Programming Internship at [CodeAlpha](https://www.codealpha.tech).

## 👤 Author

Built by Karan as part of the CodeAlpha Python Programming Internship.
