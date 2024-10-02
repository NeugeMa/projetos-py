# Funções: 
# O que é função:
'''
As funções em Python são blocos de código reutilizavel.
Funções só funcionam quando chamada!
A chamada de função é usada para executar o bloco de código dentro da função.
'''

# Produzindo código, sem função:
ano = input("Digite seu ano de nascimento:")
while not ano.isnumeric():
    ano = input("Digite seu ano de nascimento:")
ano = int(ano)

qtd = input("Diga a quantidade de garrafas: ")
while not qtd.isnumeric():
    qtd = input("Diga a quantidade de garrafas: ")
qtd = int(qtd)

#Agora produzindo com função:
def checa_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num
    
num = checa_numero("Digite um número:")
print(num)

#Fazendo uma função e verificar se eles estão na lista:
def verifica_elemento(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return True
    return False

def forca_opcao(msg,msg_erro,lista_opcao):   #forçando o usuário a escolher
    opcao = input(msg)
    while not verifica_elemento(lista_opcao,opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao
    
nomes = ['mari', 'bia','pedro','gabriel','helo','samuel']
nome = forca_opcao("Qual nome te chamou atenção? \n ->",
                    'Opção inválida',nomes)
print(nome)
contiuar_ou_nao = forca_opcao("Deseja continuar?",'(s/n)', ['s','n'])
print(contiuar_ou_nao)

#Função que retorne números pares:
lista = [2,10,99,76,34,51,20,9]
pares = []
for elem in lista:
    if elem%2==0:
        pares.append(elem) #append = adiciona a lista vazia
print(pares)

#Agora utilizando uma função:
def acha_pares(lista_numero):
    pares = []
    for elem in lista_numero:
        if elem%2==0:
            pares.append(elem)
    return pares
lista = [2,10,99,76,34,51,20,9]
filtro = acha_pares(lista)
print(filtro)
lista2 = [90,76,88,787,34,5,23,14]
filtro = acha_pares(lista2)
print(filtro)

#Fazendo um exercício que inverta a lista, de 1 à 9 ele vá alterando a ordem
lista = [1,2,3,4,5,6,7,8,9]

def inverte_lista(lista):
    for i in range(len(lista)):
        ultimo = len(lista) - 1
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
    return
inverte_lista(lista)
print(4/3,4//3)
print(9/2,9//2)
print(lista)    


#Faça uma função que recebe uma lista de números e retorna a soma dos números
lista = [1,2,3,4,5]

def soma(resultado):
    soma = 0
    for elem in resultado:
        soma += elem
    return soma 

print(soma(lista))

#Descobrindo qual o maior número dá função:
def acha_maior(lista):
    local_maior = 0
    maior = lista[local_maior]
    for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                local_maior = i
    return local_maior

lista = [90,76,88,787,34,5,23,14]
indice_maior = acha_maior(lista)
print(indice_maior, lista[indice_maior])


# Google Drive | https://docs.google.com/document/d/1MkTDNSKe85-RVgow_Kwpk00ybxyR4eRnEXvZvZGsGOU/edit

# Exercício - Pode votar ou não?
def podeVotar(nome, idade):
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False
        
a = podeVotar("Lucas",38)
print(f"a primeira resposta foi {a}")
b = podeVotar("Maira",13)
print(f"a segunda resposta foi {b}")
c = podeVotar("Pedro",18)

#Adicionando Input
nome2 = input("Digite um nome")
idade2 = int(input("Digite uma idade"))
podeVotar(nome2,idade2)

'''
- Quando eu rodo a linha a = podeVotar("Lucas",38) , eu faço duas atribuições.
nome="Lucas”, idade=38

        - Quando a função termina, ela executou o comando return True
        - Isso faz o seguinte: a = podeVotar(“Lucas”,38)  True

- Quando eu rodo a linha b = podeVotar("Maira",13) , eu faço duas atribuições.
nome=”Maira”, idade=13

        - Quando a função termina, ela executou o comando return False
        - Isso faz o seguinte: b = podeVotar(“Maira”,13)  False

'''

# Exercício - Calcular Idade
# Escreva uma função que recebe o ano de nascimento da pessoa e retorna a idade da pessoa
ano_atual = 2024

def calcularIdade(nome,ano_nascimento):
	print(f"A pessoa {nome} tem a idade {2024-ano_nascimento}")
	return  ano_atual-ano_nascimento
	
a = calcularIdade("Lucas",2004)
b = calcularIdade("Mari",1994)
c = calcularIdade("Helo",2014) 

# Exercício - Pode votar ou não? | Outra forma
def podeVotar(nome, ano_nascimento):
    idade = calculaIdade(nome, ano_nascimento)
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False
        
def calculaIdade(nome,ano_nascimento):
    print(f"A pessoa {nome} tem a idade {2024-ano_nascimento}")
    return 2024-ano_nascimento
    
        
a = podeVotar("Lucas",2004)
b = podeVotar("Rafael",1996)
c = podeVotar("Gabriela",2014)


# Exercício - Calcular Idade usando DateTime
from datetime import datetime

agora = datetime.now()
ano_atual = agora.year

def calculaIdade(nome,ano_nascimento):
    idade  = ano_atual-ano_nascimento
    print(f"A pessoa {nome} tem a idade {idade}")
    return idade
    
a = calculaIdade("Lucas",2004)
b = calculaIdade("Rafael",1996)
c = calculaIdade("Gabriela",2014)

# Exercício - Faça uma função que mostre o maior número
def maior(numeros):
    maior = 0 # A variável maior é acumulativa
    for elemento in numeros:
        if elemento >  maior:
            maior = elemento
    return maior
    

n = maior([10,20,2,30,7]) #maior retorna o 30, o n vai valer 30
n2 = maior([100,200,2,30,7]) #maior retorna o 200, o n vai valer 200
n3 = maior([-2,-3,-1]) #BUG! era pra ser -1, mas vai ser 0

