import random
import string

from words import words


def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    ans = get_word(words)
    letters = set(ans)
    alphabet = set(string.ascii_letters)
    used_letter = set()
    lives = 6
    while len(letters) > 0 and lives > 0:
        print("You have", lives, "lives and you've used these letters: ", " ".join(used_letter))
        word_list = [l if l in used_letter else "-" for l in ans]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: \n")
        if user_letter in alphabet-used_letter:
            used_letter.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)

            else:
                lives -= 1
                print("Incorrect\n")

        elif user_letter in used_letter:
            print("You have already used that letter")

        else:
            print("That is not a valid character.")
    if lives == 0:
        print("Game Over")
    else:
        print("You've won")
    print(f"The word was {ans}")
hangman()