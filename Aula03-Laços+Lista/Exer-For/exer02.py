#Peça 10 números ao usuário e faça a média e a soma
soma = 0 
media = 0 

for i in range(10):
    num = input(f"Digite números {1+i}: ")
    while not num.isnumeric():
        print("Inválido!")
        num = input(f"Digite números {1-i}: ")
    num = int(num)
    soma += num 
media = soma/10
print(f"A soma dos números é de {media}")    

# Resolução Professor:
soma = 0
for i in range(1,11):
    num = input("Diga seu número: ")
    while not num.isnumeric():
        num = input("Digite números: ")
    num = int(num)
    soma += num 
print(f"A soma é {soma} e a média é {soma/i}") #dividindo por i 