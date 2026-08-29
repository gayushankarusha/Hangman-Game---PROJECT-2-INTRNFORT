# ------------------------------------------------------------
# HANGMAN GAME PROJECT (with UTF-8 logging)
# ------------------------------------------------------------
import random

# Step 1: Define secret words
secret_words = ["apple", "banana", "mango", "orange", "grapes",
                "papaya", "cherry", "pineapple", "fig", "watermelon"]

# Step 2: Choose a random word
def choose_word():
    return random.choice(secret_words)

# Step 3: Validate guess
def validate_guess(guess, guessed_letters, log_file):
    if len(guess) != 1 or not guess.isalpha():
        message = "Invalid input! Please enter a single alphabet letter."
        print(message)
        log_file.write(message + "\n")
        return False
    if guess in guessed_letters:
        message = "You already guessed that letter."
        print(message)
        log_file.write(message + "\n")
        return False
    return True

# Step 4: Update progress
def update_progress(word, display_word, guess):
    for i in range(len(word)):
        if word[i] == guess:
            display_word[i] = guess
    return display_word

# Step 5: Main game loop
def play_game():
    word = choose_word()
    word_length = len(word)
    chances = word_length + 2
    guessed_letters = []
    display_word = ["_"] * word_length

    # Open log file with UTF-8 encoding
    with open("hangman_output.txt", "w", encoding="utf-8") as log_file:
        log_file.write("Hangman Game Log\n")
        log_file.write(f"Secret word chosen: {word}\n")
        log_file.write(f"Chances given: {chances}\n\n")

        print("Welcome to Hangman!")
        print("Guess the fruit name.")
        print("Word to guess: ", " ".join(display_word))
        print(f"You have {chances} chances.\n")

        log_file.write("Word to guess: " + " ".join(display_word) + "\n")

        while chances > 0:
            guess = input("Enter a letter: ").lower()

            if not validate_guess(guess, guessed_letters, log_file):
                continue

            guessed_letters.append(guess)

            if guess in word:
                display_word = update_progress(word, display_word, guess)
                message = "Good guess!"
                print(message)
                log_file.write(message + "\n")
            else:
                chances -= 1
                message = f"Wrong guess! Chances left: {chances}"
                print(message)
                log_file.write(message + "\n")

            progress = "Word to guess: " + " ".join(display_word)
            print(progress)
            log_file.write(progress + "\n")

            if "_" not in display_word:
                final_message = f"\nCongratulations! You guessed the word: {word}"
                print(final_message)
                log_file.write(final_message + "\n")
                break
        else:
            final_message = f"\nOut of chances! The word was: {word}"
            print(final_message)
            log_file.write(final_message + "\n")

# Run the game
play_game()
