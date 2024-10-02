'''Tendo como entrada a altura e o sexo (codificando da seguinte forma: 
1: feminino 
2: masculino) de uma pessoa, construa um programa que calcule e imprima seu peso
ideal, utilizando as seguintes fórmulas: 
            - para homens (72.7*Altura) - 58 
            - para mulheres (62.1*Altura) - 44.7 '''
            
#Exer06
altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")
if sexo == "feminino":
    peso = (62.1*altura) - 44.7
    print(f"Seu peso ideal é de {peso} kg")
    
elif sexo == "masculino":
        peso = (72.7*altura) - 58
        print(f"Seu peso ideal é de {peso} kg")
else:
    print("Opção inválida. Por favor, digite 'feminino' ou 'masculino'.")
