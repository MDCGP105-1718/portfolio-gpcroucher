def script(): # main script loop
    lives = 9
    guessed_characters = []
    word = str(input("Enter the word: ")).strip() # takes input for word as a string and removes leading and trailing whitespace
#    word = list(word) # converts word into a list of characters
    if " " in word: # if word contains a space
        return # exits the program
    print(chr(27) + "[2J") # clears the terminal
    clue = "_" * len(word)
    while lives > 0:
        print(clue)
        guess = str(input("Make a guess: ")).strip()
        if len(guess) > 1:
            print("Single characters only please.")
            continue
        if guess in guessed_characters:
            print("You already guessed this!")
            continue
        guessed_characters.append(guess)
        if guess not in word:
            lives -= 1
            print()
            continue
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
