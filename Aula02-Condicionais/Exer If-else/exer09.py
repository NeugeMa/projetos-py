'''Escreva um programa para ler 3 valores inteiros e escrever o maior deles. 
Considere que o usuário não informará valores iguais. '''

#Exer09
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    print(f"O maior número é {num1}")
    
elif num2 >= num1 and num2 >= num3:
    print(f"O maior número é {num2}")
    
else:
    #num3 >= num1 and num3 >= num2:
    print(f"O maior número é {num3}")
    
#Resolução Professor
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    print(f"O maior número é {num1}")

elif num2 > num3: 
    print(f"O maior número é {num2}")

else:
    print(f"O maior número é {num3}") 

