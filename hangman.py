import random
from word import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words).upper()  # Get a random word.
    word_letters = set(word)  # The letters of the word.
    used_letters = set()  # The used letters from the user.
    alphabet = set(string.ascii_uppercase)  # The alphabet in uppercase.
    user_lives = 7

    # Ask the user for a letter.
    while len(word_letters) > 0 and user_lives > 0:
        # Show to the user the remaining lives.
        print(f"\t\tLives: {user_lives}")
        # Show to the user the letters that have already been used.
        print("You have already used the letters: " + " ".join(used_letters))
        # Show to the user the secret word, but encrypted.
        word_characters = [letter if letter in used_letters else "-" for letter in word]
        print("Guess the word: " + " ".join(word_characters))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet and user_letter not in used_letters:
            # Add the letter to the used letters list.
            used_letters.add(user_letter)
            if user_letter in word:
                # If the guessed letter is in the word, remove it from the word_letters list.
                word_letters.remove(user_letter)
            else:
                user_lives -= 1
        elif user_letter in used_letters:
            # If the guessed letter have already been used, remind the user.
            print(f"You have already used the letter '{user_letter}'!")
        else:
            # If the user enters a character that is not in the alphabet, remind the user.
            print("Invalid character!")

    if user_lives > 0:
        print(f"Congrats! you have successfully guessed the word '{word}'")
    else:
        print(f"You lose! The word was '{word}'")


hangman()