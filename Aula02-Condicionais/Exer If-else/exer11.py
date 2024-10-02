'''Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é 
Acutângulo, Retângulo ou Obtusângulo. Sendo que:

- Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
- Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
- Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)'''
#Exer11

angulo1 = int(input("Digite o valor do primeiro angulo: "))
angulo2 = int(input("Digite o valor do segundo angulo: "))
angulo3 = int(input("Digite o valor do terceiro angulo:  "))

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90: 
    print("Triângulo Retângulo: possui um ângulo reto. (igual a 90º)")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90: 
    print("Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)")
else: 
    print("Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)")