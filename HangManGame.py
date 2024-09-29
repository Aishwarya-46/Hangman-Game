import random

# List of words to guess
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Select a random word from the list
word = random.choice(word_list)

# Initialize the game state
guesses = "_" * len(word)
incorrect_guesses = 0

while True:
    # Display the current state of the word
    print(guesses)

    # Get the player's input
    guess = input("Guess a letter: ")

    # Check if the guess is correct
    if guess in word:
        # Fill in the correct guesses
        for i, letter in enumerate(word):
            if letter == guess:
                guesses = guesses[:i] + guess + guesses[i+1:]
    else:
        # Increment the incorrect guesses
        incorrect_guesses += 1

    # Check if the player has won or lost
    if all(c != "_" for c in guesses):
        print("Congratulations! You guessed the word!")
        break
    elif incorrect_guesses >= 6:
        print("Game over! You ran out of attempts.")
        break

print("The word was:", word)