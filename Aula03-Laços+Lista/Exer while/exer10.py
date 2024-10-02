'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex: 5!=5.4.3.2.1=120
'''

notas = []
numero = int(input("Quais notas você gostaria de calcular a média?"))
i = 0 
while i < numero: 
    nota = float(input(f"Digite sua nota {i+1}:"))
    notas.append(nota)
    i+=1 

soma = sum
quantidade = len
media = soma / quantidade 

print(f"A média aritmética das notas é: ")

# Resolução Professor:
num = 5 
fatorial = num 
fatorial_string = f"{num} = {num}"

while num > 1:
    num -=1 
    fatorial*= num
    fatorial_string += f"*{num}"
fatorial += f" = {fatorial}"
print(fatorial_string)