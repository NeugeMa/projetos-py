#Peça 10 números ao usuário e conte a quantidade de pares e impares
pares = 0
impares = 0

for i in range(10):
    num = input(f"Digite números {1+i}: ")
    while not num.isnumeric():
        print("Inválido!")
        num = input(f"Digite números {1-i}: ")
    num = int(num)
    if num%2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Você digitou a quantidade de pares {pares} e a quantidade de impares {impares} ")


# Resolução Professor:
pares = 0
for i in range(1,11):
    num = input("Diga seu número: ")
    while not num.isnumeric():
        num = input("Digite números: ")
    num = int(num)
    if num%2 == 0:
        pares += 1
print(f"Você digitou {pares} pares e {i - pares} impares")