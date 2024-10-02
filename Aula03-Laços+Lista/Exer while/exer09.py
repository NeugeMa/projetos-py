'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares 
e a quantidade de números impares.
'''

qtd = 1
pares = 0
impar = 0

while qtd < 10: 
    numero = int(input(f"Diga o {qtd} número: "))
    if numero%2 == 0: 
        pares += 1
        qtd += 1
    impar += 1
    qtd += 1

print(f"Quantidade par {pares} | Quantidade impares {impar}")

#Resolução Professor: 
i = 0
pares = 0
impares = 0

while i<10: 
    num =input("Digite o {i+1} número: ")
    while not num.isnumeric(): 
        print("Erro! Digite novamente ")
        num =input("Digite o {i+1} número: ")

    num = int(num)
    if num % 2 == 0:
        pares += 1 
    
    i += 1 
print(f"O número de pares é {pares} e o número de impares é {impares}")

