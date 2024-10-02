''' Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso: 
- Caso o número de lados seja inferior a 3 escrever NÃO É UM POLIGNO
- Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
'''

#Exer08 
nm_lado = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado (em cm): "))

if nm_lado == 3:
    print("TRIÂNGULO")
    area = (medida_lado ** 2) * (3 ** 0.5) / 4
    print("Área:", area)
elif nm_lado == 4:
    print("QUADRADO")
    area = medida_lado ** 2
    print("Área:", area)
elif nm_lado == 5:
    print("PENTÁGONO")
else:
    if nm_lado < 3:
        print("NÃO É UM POLÍGONO")
    else:
        print("POLÍGONO NÃO IDENTIFICADO")

#Resolução Professor: 
lados = int(input("Digite o número de lados do polígono: "))
valor = float(input("Digite a medida do lado (em cm): "))
forma = '' 
if lados<3: 
    print("NÃO É UM POLÍGONO")
elif lados > 5: 
    print("NÃO É UM POLÍGONO")
else: 
    valor = int(input("Digite o tamanho do lado: "))
    if lados == 3: 
        forma = 'triangulo'
        perimetro = 3*valor 
    elif lados == 4:
        forma = 'quadrado'
        perimetro = 4*valor
    elif lados == 5: 
        forma = 'pentagono'
        perimetro = 5*valor

if forma: 
    print(f'Você escolheu uma {forma} com périmetro de {perimetro}')