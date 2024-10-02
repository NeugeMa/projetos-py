''' Faça um programa que peça para o usuário inserir dois números e que verifique qual é o maior ou se eles são iguais. '''

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1 > num2: 
    print(f"O número {num1} é maior que o número {num2}")

else:
    print(f"O número {num2} é maior que o número {num1}")
    
''' Faça um programa que peça para o usuário inserir dois números e que verifique qual é o menor ou se eles são iguais. '''

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1 == num2: 
    print(f"Os números {num1} e {num2} são iguais")
elif num1 <= num2: 
    print(f"O número {num1} é menor ao número {num2}")

else: 
    print("Resposta Inválida")