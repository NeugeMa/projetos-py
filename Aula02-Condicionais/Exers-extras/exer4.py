''' Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos 
e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter 
e mostre na tela uma mensagem de sua escolha.'''

pergunta = input("Você tem algum irmão? (Sim ou Não): ")
if pergunta == 'Sim': 
    print("Que legal!!")
    irmaos = int(input("Quantos irmãos você tem? "))
    
elif pergunta == 'Não': 
    print("Que pena")
    irmaos_qtd = input("Mas você gostaria de ter? (Sim ou Não): ")

else: 
    print("Resposta inválida")