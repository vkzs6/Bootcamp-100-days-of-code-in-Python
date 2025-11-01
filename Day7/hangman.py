import random
import man_module
import string


words = [
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



def select_a_word():

    word_temp = random.choice((words))
    return word_temp




hangman = True
selected_word = str()


selected_word = select_a_word()
qty_words = len(selected_word)

# print(selected_word)

test_word = "aaa-bbb-ccc"
temp_word = test_word

corret_word = []
while hangman == True:
    
    char = input("\nGuess a word: ")
    word_chosed = []
    for word in test_word:
        if char == word_chosed:
            break
        elif char == word:
            ind = test_word.index(char)
            corret_word.insert(ind,char)
            word_chosed.insert(char)
        else:
            print("_", end=" ")
    
    
    
    print(corret_word, end=" ")
    


    


            
    
            

    
    


print("Finish")