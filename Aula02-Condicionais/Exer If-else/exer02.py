'''Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mnesagem que diga 
se ela poderá ou não votar esse ano (não é necessário considerar o mês em que ela nasceu)'''

#Código de Votação
#Exer02
ano = int(input("Digite seu ano de nascimento: "))
if ano <= 2008:  
    print("Você poderá votar esse ano!! Faça o L ou Arma")

else: 
    print("Espere mais um pouco, e poderá votar!")

#Resolução Professor:
ano = int(input("Digite seu ano de nascimento: "))
idade = 2024 - ano
if idade >= 18:
    print("É obrigatório votar!")
elif idade >= 16: 
    print("É opcional votar!")
else: 
    print("Não pode votar!")
