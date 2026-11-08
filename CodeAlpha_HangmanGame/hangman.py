
import random

# Predefined words
words = ["python", "computer", "program", "developer", "keyboard"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("\n================================")
print("       WELCOME TO HANGMAN")
print("================================")

# Main game loop
while incorrect_guesses < max_attempts:

    display_word = ""

    # Display guessed and hidden letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", incorrect_guesses)
    print("Remaining attempts:", max_attempts - incorrect_guesses)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    # Get user input
    guess = input("\nGuess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Enter one alphabet only.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Losing condition
if incorrect_guesses == max_attempts:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")
