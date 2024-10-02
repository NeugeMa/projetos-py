#0.1
#Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos da lista.

lista = [1, 2, 3, 4, 5]
def soma_lista(lista):
    return sum(lista)

#0.2
#Crie uma função que receba uma lista de números e retorne o mais elemento da lista.

lista = [1, 2, 3, 4, 5]
def maior_elemento(lista):
    return max(lista)

#0.3
# Faça uma função que receba uma lista de strings e retorna uma nova lista contendo apenas as strings que começam com a letra 'a'.

def filtra_a(lista):
    return [s for s in lista if s.startswith('a')]  

#0.4
'''
Escreva uma função que receba uma lista de números e retorne uma nova lista contendo apenas os 
números pares.
'''
def filtra_pares(lista):
    return [num for num in lista if num % 2 == 0]


#0.5
'''
Crie uma função que receba uma lista de palavras e retorne o número de cada 
letra em cada palavra como uma nova lista
'''
def contar_letras(lista):
    resultado = []
    for palavra in lista:
        contador = {}
        for letra in palavra:
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
        resultado.append(contador)
    return resultado

#0.6
'''
Faça um função que receba duas listas e retorne uma lista contendo os elementos comuns entre as duas listas.
'''
def elementos_comuns(lista1, lista2):
    return list(set(lista1) & set(lista2))