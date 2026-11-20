import random

# List of five predefined words
words = ["python", "computer", "program", "keyboard", "coding"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")

while incorrect_guesses < max_attempts:
    # Display correctly guessed letters and hide the rest
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    # Check whether the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over! You lost.")
    print("The correct word was:", word)
