''' Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida. '''

escolha = input("Escolha uma das três bebidas: 1. Coca-Cola, 2. Guaraná, 3. Fanta:")
if escolha == '1': 
    print("Você escolheu Coca-Cola")

elif escolha == '2':
    print("Você escolheu Guaraná")
    
else: 
    print("Você escolheu Fanta")
    
#Resolução ChatGPT 
print("Escolha uma das opções de bebidas:")
print("1. Café")
print("2. Chá")
print("3. Suco de laranja")

escolha = input("Digite o número da bebida desejada: ")

if escolha == "1":
    print("Você escolheu Café.")
elif escolha == "2":
    print("Você escolheu Chá.")
elif escolha == "3":
    print("Você escolheu Suco de laranja.")
else:
    print("Opção inválida. Por favor, escolha um número de 1 a 3.")
