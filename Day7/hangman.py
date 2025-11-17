import random
import man_module
import string
import os # This import it's to clear the console
# STEP 1

# TO DO - 1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TO DO - 2: Ask the user to guess a letter and assign their answer to a variable called guess, Make guess lowercase.
# TO DO - 3: Chek if the letter the user guessed (guess) is one the letters in the chosen_word.

end_of_game = False

hangman_list = [ 
r"""
      _______
     |/      |
     |       
     |       
     |       
     |       
     |
   __|___
""",
r"""
      _______
     |/      |
     |      (_)
     |       
     |       
     |       
     |
   __|___
""",
r"""
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |       
     |
   __|___
""",
r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |       
     |
   __|___
""",
r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
   __|___
""",
r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
   __|___
""",
r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / /
     |
   __|___
"""
]

word_list = [
    "electricity", "computer", "hardware", "circuit", "robot", "memory", "power", "submarine",
    "chess", "resistance", "matrix", "function", "laser", "mechanism", "bodyguard", "titanic",
    "global", "ozone", "bridge", "technology", "spider", "pyramid", "sphere", "member",
    "warning", "yourself", "screen", "language", "system", "internet", "parameter", "traffic",
    "network", "filter", "nucleus", "automatic", "microphone", "cassette", "operation", "country",
    "beautiful", "picture", "teacher", "superman", "undertaker", "alarm", "process", "keyboard",
    "electron", "certificate", "grandfather", "landmark", "relativity", "eraser", "design",
    "football", "human", "musician", "egyptian", "elephant", "queen", "rec", "message",
    "wallpaper", "nationality", "answer", "wrong", "statement", "forest", "puzzle", "voltage",
    "current", "mathematics", "wisdom", "dream", "supermarket", "database", "collection",
    "barrier", "project", "sunlight", "figure", "graph", "battle", "hundred", "signal",
    "thousand", "transformation", "daughter", "flower"
]

# DEFS
def randomly_word():

    word_temp = random.choice((word_list))
    return word_temp

def ask_to_user():

    word_input= input("\nGuess a word: ")
    return word_input

# GLOBAL VARIABLES

display = []
lives_out = int(0)
guess = str() # variable choosed for the user
tries = 0

chosen_word = randomly_word() # it select a random word by the function
word_lenght = len(chosen_word)


for _ in chosen_word: # it's inicializate the display
    display += "_"

print(f"The chosen_word is: {chosen_word}") 

while not end_of_game:

  # Check guessed letter.
  # print('\n' * 130) 
  print(hangman_list[lives_out])
  print(f"{' '.join(display)}") # Join all the elements in the list and turn it into a string.
  guess = input("\nGuess a word: ")

  for position in range(word_lenght):
      letter = chosen_word[position]
      if guess == letter:
          display[position] = guess # it's make a swap between "_" and corret letter
          tries += 1
  if guess not in chosen_word:
    lives_out += 1
    if lives_out == 6:
       end_of_game = True
       print("You Lose!")
       print("Try again")
  if "_" not in display:# Check if user has got all letters.
    end_of_game = True
    print("CONGRADTULATIONS YOU WIN!!")
    print(f"Tries: {tries}")






