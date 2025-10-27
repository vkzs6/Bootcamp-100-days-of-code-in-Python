#  - Projeto: Bootcamp - 100 Days of Code – The Complete Python 
#  - Arquivo: strong_password_generator.py
#  - Desenvolvedor: Arthur de Queiroz
#  - Data: Outubro/2025
#  - Descrição: Criando um gerador de senhas fortes mesclando letras numeros e simbolos
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the Password Generator")

amount_of_letters = int(input("\nHow many letters would you like in your password? "))
amount_of_numbers = int(input("\nHow many numbers would like? "))
amount_of_symbols = int(input("\nHow many symbols would like? "))

sum_of_characteres = amount_of_letters + amount_of_numbers + amount_of_symbols
password = str("")
while len(password) < sum_of_characteres:

    randomif = random.randint(0,2)
    if randomif == 0 and amount_of_letters > 0:# if 0, starts add the amount of letters solicited, until of the amount of letters be greather then 0  
        position_letter = random.randint(0,51)
        temp_letter = letters[position_letter]
        password += temp_letter
        amount_of_letters -= 1
    if randomif == 1 and amount_of_symbols > 0:
        position_symbol = random.randint(0,8)
        temp_symbol = symbols[position_symbol]
        password += temp_symbol
        amount_of_symbols-= 1
    if randomif == 2 and amount_of_numbers > 0:
        position_number = random.randint(0,9)
        temp_number = numbers[position_number]
        password += temp_number
        amount_of_numbers-= 1

print(f"Here is your password: {password}")
# if amount_of_numbers < 0:
    

# if amount_of_symbols < 0:
    
