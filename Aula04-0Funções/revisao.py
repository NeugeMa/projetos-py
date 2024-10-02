#Revisão de funções	:)

#Função que soma 
def soma_lista (lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma

def media_lista (lista):
    soma = soma_lista(lista) #Chamando uma funcão dentro de outra função
    media = soma/len(lista)
    return media

#Forçando uma opção 
def meu_in(lista, buscar):
    for elem in lista:
        if elem == buscar:
            return True
    return False

def meuIndex(lista,buscar):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return i
    return False

def forca_opcao(msg,lista_opcao):
    msg_erro = ''.join(lista_opcao)
    msg_erro = f"Somente estas opções: \n {msg_erro}"
    opcao = input(msg)
    while not meu_in(lista_opcao,opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao

carros = ['up','gol','celta','uno','land'] #Carros é uma variável global
preco = [10,15,898,50,5]
indice_escola = meu_index(carros,'escolha') 
valor_escolha = preco[indice_escola]
print(f"O carro escolhido custa {valor_escolha} reais")

escolha = forca_opcao("Qual carro você gostaria de comprar?",carros)
sim_ou_nao = ['sim','não']
escolha = forca_opcao("Deseja continuar?",sim_ou_nao)


#Fazendo uma recursão
def verifica_numero(msg): #Produzindo um while sem utilizar um while
    num = input(msg)
    if not num.isnumeric():     #Se não for:
        print("Digite um número válido")
        num = verifica_numero(msg) 
    return int(num)
num = input("Digite um número:"	)
print(num)


#Fazer uma função que ache uma lista dentro de outra lista:
def acha_lista(lista,lista2):
    for i in range(len(lista)):
        if lista[i:i+len(lista2)] == lista2:
            return True
    return False

lista = [1,2,3,4,5,6,7,8,9]
lista2 = [5,6,7]
print(acha_lista(lista,lista2))




