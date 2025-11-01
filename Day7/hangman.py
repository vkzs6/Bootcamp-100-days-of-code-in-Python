import random
import man_module
import string

# STEP 1

# TO DO - 1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TO DO - 2: Ask the user to guess a letter and assign their answer to a variable called guess, Make guess lowercase.
# TO DO - 3: Chek if the letter the user guessed (guess) is one the letters in the chosen_word.

hangman = True

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


def randomly_word():

    word_temp = random.choice((word_list))
    return word_temp





guess = str() # variable choosed for the user
chosen_word = randomly_word() # it select a random word by the function

print(f"The chosen_word is: {chosen_word}") 

while hangman == True:
    
    guess = input("\nGuess a word: ")
    for word in chosen_word:
        if guess == word:
            print("Right", end = " ")
        else:
            print("Wrong", end=" ")
    


    


            
    
            

    
    


print("Finish")