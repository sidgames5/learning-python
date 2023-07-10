# https://www.youtube.com/watch?v=rfscVS0vtbw
# left off at 2:32:44

secret_word = "supercalifragilisticexpialidocious"
guess = ""
guesses = 1
guess_limit = 3

guess = input("Enter a guess: ")
while guess != secret_word:
    if (guesses >= guess_limit):
        print("You failed! The word is " + secret_word)
        break
    print("Wrong!")
    guess = input("Guess again: ")
    guesses += 1


if (guesses < guess_limit):
    print("You got it in " + str(guesses) + " tries!")
