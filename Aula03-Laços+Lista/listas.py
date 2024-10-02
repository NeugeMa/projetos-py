# Aprendendo For - 03/5

# O que é Lista?
#  Uma lista pode conter qualquer tipo de informação, como números, palavras, objetos, entre outros.

lista = [6, True, 'mari', [], 4.2]
#lista possui indice, sendo o primeiro 0, exemplo:
print(lista[0]) #o indice inicia em 0, e nossa primeira informação é 6 
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

#Uma forma mais eficiente de usar: 
lista = [6, True, 'mari', [], 4.2]
for i in range(len(lista)):
    print(lista[i])

for elemento in lista:
    elemento = 1
    print(elemento)

#Utilizando append
num = input("Diga um número: ")
lista = []
lista.append(1)
print(lista)
lista.append(111)   #adiciona ao fim da lista 
print(lista)
