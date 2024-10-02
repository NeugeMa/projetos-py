'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo 
é aquele que é divísivel somente por ele mesmo e por 1. 
'''

num = int(input("Digite um número: "))

# Verificando se o produto é primo
if num > 1:
    i = 2
    while i < num:
        if (num % i) == 0:
            print(f'{num} é um número primo')
            break
        i += 1
    else:
        print(f'{num} não é um número primo')
else:
    print(f'{num} não é um número primo')


# Resolução Professor:
