'''
Faça um programa que calcule e mostre a média aritméticade N notas. 
'''

while True:
    num = int(input("Digite um número: "))
    if num > 0:
        break
    print("Erro! Digite sua nota")

total = 0
count = 0

while count < num:
    nota = float(input("Digite sua nota: "))
    total += nota
    count += 1

media = total / num
print(f'A média aritmética das notas é: {media}')