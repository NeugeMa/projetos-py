''' Faça um programa que peça para o usuário inserir dois números, pergunte se ele quer realizar a operação de adição ou de 
subtração e, que a partir desta escolha, mostre o resultado na tela.'''

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
operacao = input("Deseja realizar a operação de adição (1) ou subtração (2)?")

# Verifica a escolha do usuário e realiza a operação correspondente
if operacao.lower() == "1":
    resultado = num1 + num2
    print(f"O resultado da adição de {num1} e {num2} é: {resultado}")
    
elif operacao.lower() == "2":
    resultado = num1 - num2
    print(f"O resultado da subtração de {num1} e {num2} é: {resultado}")
    
else:
    print("Opção inválida. Por favor, escolha 'adição' ou 'subtração'.")
    
    
'''  Faça um programa que peça para o usuário inserir dois números, pergunte se ele quer realizar a operação de multiplicação ou de divisão e que, a partir desta escolha, mostre o resultado na tela. '''

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
operacao = input("Deseja realizar a operação de multiplicação (1) ou divisão (2)?")

# Verifica a escolha do usuário e realiza a operação correspondente
if operacao.lower() == "1":
    resultado = num1 * num2
    print(f"O resultado da multiplicação de {num1} e {num2} é: {resultado}")
    
elif operacao.lower() == "2":
    resultado = num1 / num2
    print(f"O resultado da divisão de {num1} e {num2} é: {resultado}")
    
else:
    print("Opção inválida. Por favor, escolha 'adição' ou 'subtração'.")