#  - Projeto: Bootcamp - 100 Days of Code – The Complete Python 
#  - Arquivo: variable.py
#  - Desenvolvedor: Arthur de Queiroz
#  - Data: Outubro/2025
#  - Descrição: Desenvolvendo o aprendizado utilizando o uso de desvio condicional junto a lógica de programação em python. 

import random

#Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

picked = int(input("What do you choose? Type 0 for rock 1, 1 for paper and 2 for scissors!\nYour entry: "))

picked_for_computer = random.randint(0,2)

if picked == 0:
    if picked_for_computer == 0:
        print(f"\nYour choice \n {rock}")
        print(f"The choice of computer \n {rock}")
        print("TIE :( ")
    if picked_for_computer == 1:
        print(f"\nYour choice \n {rock}")
        print(f"The choice of computer \n {paper}")
        print("\nYOU LOSE")
    if picked_for_computer == 2:
        print(f"\nYour choice \n {rock}")
        print(f"The choice of computer \n {scissors}")
        print("\nYOU WIN")
elif picked == 1:
    if picked_for_computer == 0:
        print(f"\nYour choice \n {paper}")
        print(f"\nThe choice of computer \n {rock}")
        print("\nYOU WIN")
    if picked_for_computer == 1:
        print(f"\nYour choice \n {paper}")
        print(f"The choice of computer \n {paper}")
        print("\nTIE :( ")
    if picked_for_computer == 2:
        print(f"\nYour choice \n {paper}")
        print(f"The choice of computer \n {scissors}")
        print("\nYOU LOSE")
elif picked == 2:
    if picked_for_computer == 0:
        print(f"\nYour choice \n {scissors}")
        print(f"\nThe choice of computer \n {rock}")
        print("\nYOU LOSE")
    if picked_for_computer == 1:
        print(f"\nYour choice \n {scissors}")
        print(f"The choice of computer \n {paper}")
        print("\nYOU WIN")
    if picked_for_computer == 2:
        print(f"\nYour choice \n {scissors}")
        print(f"\nThe choice of computer \n {scissors}")
        print("\nTIE :( ")
        
else:
    print("Your entry isn't valid! - ERR0R")

