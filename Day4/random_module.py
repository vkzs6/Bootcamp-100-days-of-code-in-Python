#  - Projeto: Bootcamp - 100 Days of Code – The Complete Python 
#  - Arquivo: variable.py
#  - Desenvolvedor: Arthur de Queiroz
#  - Data: Outubro/2025
#  - Descrição: Aprendendo sobre modulos, em especifico sobre 
 
# NEW COMMAND - CTRL + D : HELPFUL FOR SELECT ONE OR ALL CHARACTERS WITH OBJECTIVE TO CHANGE OR DELETE THEM
import random
# import my_module

# print(my_module.pi)

random_integer = random.randint(0,4)
# print(f"The random number it's {random_integer}")

random_float = random.random()
# print(f"The random number it's {random_float}")

# How to generate a float number between 0 and 5

#TIP 1: Using a random integer number summed on random float point number
random_number = random_integer + random_float
print(f"The random number it's {random_number}")

#TIP 2: Making a mutiplication by 5

random_number1 = (random_float * 5)
print(f"The random number it's {random_number1}")