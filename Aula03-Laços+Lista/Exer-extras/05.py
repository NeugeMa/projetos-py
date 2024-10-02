'''
5. Faça um programa, utilizando while e listas, que permita o usuário realizar o cadastro de um número indeterminado de pessoas 
enquanto quiser e os mostre na tela ao finalizar.
'''

nomes = [] 
continuar = "sim"

while continuar == "sim":
    nome = input("Digite um nome: ")
    nomes.append(nome)
    continuar = input("Deseja continuar? (sim/não): ")
    
for nome in nomes:
    print(nome)