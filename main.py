# https://www.youtube.com/watch?v=rfscVS0vtbw
# left off at 3:00:18

import random


def translate(phrase):
    result = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            result += str(random.randint(0, 9))
        else:
            result += letter
    return result


phrase = input("Enter a phrase: ")
print(translate(phrase))
