# /*
#  * Projeto: Bootcamp - 100 Days of Code – The Complete Python 
#  * Arquivo: tip_calculator.py
#  * Desenvolvedor: Arthur de Queiroz
#  * Data: Outubro/2025
#  * Descrição: Aplicação de f-string junto a função round para limitar as casas decimais de um float
#  */ 
print("Seja bem vindo ao calculador de gorjetas!")
valor_conta= float(input("Qual é o valor total da conta? $"))
percentual = float(input("Qual o percentual de gorjeta que vocês querem deixar? 10, 12 ou 15? "))
percentual /=100
pessoas_pagantes = int(input("Vão dividir a conta em quantas pessoas? "))
valor_conta += (percentual * valor_conta) 
valor_por_pessoa = (valor_conta / pessoas_pagantes)
print(f'Cada pessoa deve pagar: $ {round(valor_por_pessoa,4)}') 