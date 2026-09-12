import random

def hangman():
    words = ["python", "hangman", "programming", "developer", "computer"]
    word = random.choice(words)
    guessed = set()
    attempts_left = 6

    print("Welcome to Hangman! Guess the word.")

    while attempts_left > 0:
        display = "".join(letter if letter in guessed else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Attempts left: {attempts_left}")

        if "_" not in display:
            print(f"🎉 You won! The word was '{word}'.")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess not in word:
            attempts_left -= 1
            print(f"'{guess}' is not in the word.")

    print(f"\n💀 Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()