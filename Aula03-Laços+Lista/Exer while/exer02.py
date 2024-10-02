'''
Faça um programa que leia e válide as seguintes informações:
a. Nome: maior que 3 caracteres; 
b. Idade: entre 0 e 150;
c. Sálario: maior que 0;
d. Sexo: f ou m;
e. Estado Civil: s,c,v,d;
'''

while True: 
    letra = input("Digite seu nome: ")
    if len(letra)>3:                   # Len (conta caracter)
        break 
    print("Resposta inválida")

while True:
    idade = input("Digite um número: ")
    if idade.isnumeric(): 
        if int(idade) >= 0 and int(idade) <= 150: 
            break 
    print("Resposta inválida")

while True:
    salario = input("Digite seu salário: ")
    if salario.isnumeric(): 
        salario = int(salario)
        if salario > 0: 
            break 

while True:
    sexo = input("Digite seu sexo, (f)eminino e (m)asculino: ")
    if len(sexo) == 1:
        if sexo == "f" or "m": 
            break
''' Uma forma de se fazer 
sexo = input("Digite seu sexo | (f)eminino ou (m)asculino")
while not (sexo == 'f' or sexo == ' m'): # while sexo != "f" and sexo != "m": 
    sexo = input("Digite seu sexo | (f)eminino ou (m)asculino")
'''
        
while True: 
    estado = input("Digite seu estado civil: \n (s)olteiro \n (c)asado \n (v)iuvo \n (d)ivorciado: ")
    if len(estado) == 1: 
        if estado == 's' or 'c' or 'v' or 'd': 
            break
print(f"Olá {letra} você possui {idade} anos, seu sexo é {sexo}, seu estado cívil é {estado} e por final seu salário é de {salario}")