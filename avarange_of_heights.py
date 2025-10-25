#  - Projeto: Bootcamp - 100 Days of Code – The Complete Python 
#  - Arquivo: variable.py
#  - Desenvolvedor: Arthur de Queiroz
#  - Data: Outubro/2025
#  - Descrição: Calculando a média da altura de alunos com listas e loops



students_heights = [] #Inicializate the list
num_of_students = 3
for _ in range(num_of_students): #it's making a loop for walk each position of the list.
    try:
        students_heights.append(float(input("Enter with the heights: ")))
    except ValueError:
        print("The provide value isn't float number")
    
print(students_heights)

sum_of_heights = 0

for heigth in students_heights:
    sum_of_heights += heigth

avarange_of_heights = float(sum_of_heights/num_of_students)

print(f"The avarange it's: {avarange_of_heights}")
