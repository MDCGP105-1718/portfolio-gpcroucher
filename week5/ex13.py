import os

def script(): # main script loop
    lives = 9
    guessed_characters = []
    word = str(input("Enter the word: ")).strip() # takes input for word as a string and removes leading and trailing whitespace
#    word = list(word) # converts word into a list of characters
    if " " in word: # if word contains a space
        return # exits the program
    os.system("cls") # clears the terminal
    clue = "_" * len(word) # constructs a clue with underscores
    while lives > 0:
        print(clue) # show letters correctly guessed along with gaps
        guess = str(input("Make a guess: ")).strip() # takes in a guess, discarding whitespace
        if len(guess) != 1: # if guess is not a single character
            print("Single characters only please.")
            continue # back to prompt
        if guess in guessed_characters: # if guess already guessed
            print("You already guessed this!")
            continue # back to prompt
        guessed_characters.append(guess) # add to list of guessed characters
        if guess not in word: # if guess is wrong
            lives -= 1 # lose a life (starts at 9)
            print(pic[lives]) # print the corresponding hanged man
            continue # back to prompt
        for i in findOccurences(word, guess):
            s = list(clue)
            s[i] = guess
            clue = str(s)

def findOccurences(s, ch): # https://stackoverflow.com/a/13009866
    print([i for i, letter in enumerate(s) if letter == ch])
    return [i for i, letter in enumerate(s) if letter == ch] # returns a list of indexes in the source string which match a given letter

pic = [
"""
   _____
   |    o
   |   /|\
   |   / \
-------""",
"""
   _____
   |    o
   |   /|\
   |   /
-------""",
"""
   _____
   |    o
   |   /|\
   |
-------""",
"""
   _____
   |    o
   |   /|
   |
-------""",
"""
   _____
   |    o
   |    |
   |
-------""",
"""
   _____
   |    o
   |
   |
-------""",
"""
   _____
   |
   |
   |
-------""",
"""

   |
   |
   |
-------""",
"""
-------""",
""
]

while True:
    script()
