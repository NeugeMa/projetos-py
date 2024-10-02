'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
soma = 0 
contador = 0
while True:
    # Programa está vendo se todos os valores inseridos são números
    num1 = input("Digite o primeiro número:")
    num2 = input("Digite o segundo número:")
    num3 = input("Digite o terceiro número:")
    num4 = input("Digite o quarto número:")
    num5 = input("E por fim, digite o quinto número: ")
    
    if num1.isnumeric() and num2.isnumeric() and num3.isnumeric() and num4.isnumeric() and num5.isnumeric():
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        num4 = int(num4)
        num5 = int(num5)
        
        if num1 != 0:
            soma += num1
            contador += 1
        if num2 != 0:
            soma += num2
            contador += 1
        if num3 != 0:
            soma += num3
            contador += 1
        if num4 != 0:
            soma += num4
            contador += 1
        if num5 != 0:
            soma += num5
            contador += 1
        break
    else: 
        print("Digite apenas números")

media = soma / contador if contador != 0 else 0
print (f"A soma dos números é {soma} e a média é {media}")

#Resolução Professor: 
qtd = 0
soma = 0 
while qtd < 5: #Ele se repete 5 vezes, não tendo a necessidade de fazer 5 inputs
    numero = input(f"Diga o {qtd+1} número: ")
    while not numero.isnumeric():
        print("Erro! Digite um número")
        numero = input(f"Diga o {qtd+1} número:")
    numero = int(numero)
    soma += numero
    qtd += 1
print(f"A soma é de {soma}")
print(f"A média é {soma/qtd}")
