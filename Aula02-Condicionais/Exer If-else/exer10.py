'''Escreva um programa que leia as medidas dos lados de um triângulo e escreva
se ele é Equilátero, Isóceles ou Escaleno. Sendo que:
- Triângulo Equilátero: possui os 3 lados iguais 
- Triângulo Isósceles: possui 2 lados diferentes
- Triângulos Escaleno: possui 3 lados diferentes '''


lad1_medida = int(input("Digite a medida do lado do triângulo: "))
lad2_medida = int(input("Digite a medida do segundo lado do triângulo: "))
lad3_medida = int(input("Digite a medida do terceiro lado do triângulo: "))

if lad1_medida == lad2_medida == lad3_medida:
    print("Triângulo Equilátero")
elif lad1_medida == lad2_medida or lad1_medida == lad3_medida or lad2_medida == lad3_medida:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")

#Resolução Professor:
lad1_medida = int(input("Digite a medida do lado do triângulo: "))
lad2_medida = int(input("Digite a medida do segundo lado do triângulo: "))
lad3_medida = int(input("Digite a medida do terceiro lado do triângulo: "))

if lad1_medida == lad3_medida and lad1_medida == lad2_medida: 
        print("Triângulo Equilátero")
elif lad3_medida == lad2_medida or lad1_medida == lad3_medida  or lad1_medida == lad2_medida: 
      print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")