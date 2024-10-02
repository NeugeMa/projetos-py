'''As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e 
R$ 0,25 se forem compradas pelo menos 12. Escreva um programa que leia o número 
de maçãs compradas, calcule e escreva o custo total da compra.'''

#Exer04
fruta = int(input("Digite quantas maças você comprou na feira hoje? "))
if fruta >= 12:
    print(f"O valor da sua compra foi de {fruta}")

#Resolução Professor:
qtd = int(input("Digite quantas maças você comprou na feira hoje? "))
preco = 0.3
if qtd >= 12: 
    preco = 0.25 
    print({qtd})