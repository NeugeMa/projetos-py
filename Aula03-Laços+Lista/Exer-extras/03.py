'''
3. Faça um programa, utilizando while e listas, que permita o usuário escrever o nome de cinco pessoas 
e os mostre na tela.
'''

nomes = []
qtd = 1
while len(nomes) < 5: 
    nome = input(f"Diga o {qtd} nome: ")	
    nomes.append(nome)
    
for nome in nomes: 
    print(nome)
    
    
    