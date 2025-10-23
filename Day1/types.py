# /*
#  * Projeto: Bootcamp - 100 Days of Code – The Complete Python 
#  * Arquivo: types.py
#  * Desenvolvedor: Arthur de Queiroz
#  * Data: Outubro/2025
#  * Descrição: entendendo tipos e conversão para outros tipos a partir do input padrão(str)
#  */ 
num_char = len(input("What is your name?"))

new_num_char = str(num_char)

print(type(num_char))
print(type(new_num_char))