# /*
#  * Projeto: Bootcamp - 100 Days of Code – The Complete Python 
#  * Arquivo: rollercoaster.cpp
#  * Desenvolvedor: Arthur de Queiroz
#  * Data: Outubro/2025
#  * Descrição: Exemplificação dos desvios condicionais em python.
#  */ 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill =0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Who old are you?"))
    if age < 12:
        print("Child tickets are $5 USD")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7 USD")
        bill = 7
    elif age >= 45 and  age <= 55:
        print("Everything to be ok, have a free ride on us")
    else:
        print("Adult tickets are $12 USD")
        bill = 12

    wants_photo = input("Do you want a photo kaken? Y or N.")
    if wants_photo == "Y":
        #add $3 to the bill
        bill += 3  

    print(f"You final bill it's {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")