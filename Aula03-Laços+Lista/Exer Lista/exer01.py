#Declare uma lista com 10 números. Faça a soma e a média dos  números loopando nela
lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0 

for i in range(len(lista)):
    soma += lista[i]
print(soma)


# Resolução Professor:
lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0 

for num in lista: 
    soma += num
print(soma,soma/len(lista))