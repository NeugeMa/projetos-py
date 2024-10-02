'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual número ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo abaixo:

tabuada do 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 
...
5 x 10 = 50
'''

while True:
    num = input("Digite um número entre 1 e 10 para ver a tabuada: ")
    
    if num.isnumeric() and 1 <= int(num) <= 10:
        num = int(num)
        break
    else:
        print("Erro! Digite entre 1 e 10.")

print(f"Tabuada do {num}:") 
for i in range(1, 11):                      
    print(f"{num} x {i} = {num * i}")
    
# Forma de fazer utilizando apenas o While 
num = int(input("Digite um número: "))
i = 1 # Valor inicial, para que a multiplicação começe com 1 

while i <= 10: 
    resultado = num * i 
    print(f"{num} x {i} = {resultado}")
    i += 1 

# Resolução Professor:
while True: 
    hum = input("Digite um número: ")
    if num.isnumeric():
        num = int(num)
        if num > 0 and num < 10: 
            break 
num = 1 #para fazer todas as tabuadas 
while num < 10: 
    print(f"{num}x{i} = {num*i}")
    i += 1 
num += 1 