'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
1. Esse funcionário foi contratado em 1995, com sálario inicial de R$1.000,00;
2. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
3. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual 
do ano anterior. 

Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

sal_inicio = float(input("Digite o salário inicial do funcionário: "))

ano_contratacao = 1995
sal_atual = sal_inicio

while ano_contratacao <= 2022:
    if ano_contratacao > 1995:
        percentual = (ano_contratacao - 1995) * 2
        aumento = sal_atual * (percentual / 100)
        sal_atual += aumento
    ano_contratacao += 1

print(f"O salário atual do funcionário é R${sal_atual:.2f}")

salario = 1000
partida = 1995
taxa = 0.015

while partida < 2000:
    salario *= 1 + taxa 
    taxa *= 2 
    partida += 1
print(salario)