''' Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em 
ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela. '''

nome = input("Digite seu nome:")
resposta = input("Você gosta do seu nome? (Sim ou Não): ")

if resposta == "Sim":
    print("Que bom, é um lindo nome!!")

else: 
    print("Que pena")