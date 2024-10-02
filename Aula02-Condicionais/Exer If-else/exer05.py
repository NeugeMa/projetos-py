'''Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e 
escrevê-los em ordem crescente.'''

#Exer05
a = int(input("Digite a primeira letra : "))
b = int(input("Digite a segunda letra: "))
c = int(input("Digite a terceira letra: "))

if a > b and a > c: 
    aux = a     #Guarda um valor, assim não precisando utilizar a mesma váriavel 
    a = c 
    c = aux 
elif b > c: 
    aux = b 
    b = c 
    c = aux 

#Verificando se é necessário a troca de valores  
#Achando o maior elemento

#Achando o menor elemento
menor = a 
if b < menor: 
    menor = b 
    if c < menor : 
        menor = c 
#Achando o valor do meio 
meio = a + b + c - menor - maior 
print()
#Exemplo de lógica 
''' 
A B C
3 1 2 - trocar 3 por 2
2 1 3 - trocar 2 por 1 
1 2 3 
'''