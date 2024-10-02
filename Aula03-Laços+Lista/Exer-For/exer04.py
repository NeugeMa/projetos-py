#Faça a tabuada de todos os números de 1 à 10: 
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

#Resolução Professor:
#utilizando while | While dentro de um While 
i = 2 
while i <= 10: 
    print(f"Tabuada do {i}: ")
    j = 1   #ele está aqui para sempre voltar a valer 1 
    while j <= 10: 
        print(f"{i} * {j} = {i*j}")
        j += 1
    i += 1
    print()

#utilizando for
for i in range(1, 11): 
    print(f"Tabuada dp {i}:")
    for j in range (1, 11):
        print(f"{i} * {j} = {i*j}")
    print()