'''Escreva um programa para ler um número de lados de um polígono regular e a medida do lado (em cm).
Calcular e imprimir o seguinte: 
- Se o número de lados for igual a 3 escreva TRIÂNGULO e o valor da área'
- Se o número de lados for igual a 4 escreva QUADRADO e o valor da área'
- Se o número de lados for igual a 5 escreva PENTÁGONO. 
'''
#Exer07 
nm_lado = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado (em cm, por favor): "))

if nm_lado == 3:
    area = 3*medida_lado
    print("TRIÂNGULO")
    print("Área:", area)
elif nm_lado == 4:
    area = 2*medida_lado
    print("QUADRADO")
    print("Área:", area)
elif nm_lado == 5:
    print("PENTÁGONO")
else:
    print("Digito errado, refaça por favor!")

#Resolução Professor:
nm_lado = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado (em cm, por favor): "))
if nm_lado == 3:
    forma = 'triangulo'
    perimetro = 3*medida_lado
elif nm_lado == 4: 
    forma = 'quadrado'
    perimetro = 4*medida_lado
else: 
    forma = 'pentágono'
    perimetro = 5*medida_lado
    print(f"Você escolheu {forma} com périmetro {perimetro}")