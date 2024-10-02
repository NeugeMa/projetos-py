'''
Faça um programa que implemente um menu onde o usurário deverá selecionar 1 ou 0. Caso seja entrado
um número diferente, o programa deverá solicitar uma nova opção.
'''

while True: 
    opcao = input("Digite 1 ou 0: ")
    if opcao.isnumeric(): 
        opcao = int(opcao)
    
        if opcao == "1" and opcao == "0":
            print(f"Você digitou {opcao}")
        else: 
            print(f"Opção inválida")
            