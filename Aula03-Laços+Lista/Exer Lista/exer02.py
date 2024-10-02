#Declare uma lista com 10 números. Coloque os pares em uma nova lista e os impares também
lista = [1,2,3,4,5,6,7,8,9,10]
pares = []
impares = []

for i in range(len(lista)):
    if lista[i] % 2 == 0: 
        pares.append(lista[i])
    impares.append(lista[i])
print(pares)
print(impares)