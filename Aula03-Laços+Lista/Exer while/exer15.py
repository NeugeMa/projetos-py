'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1, 2, 3, 4 - Votos para os respectivos canditados
(você deve montar a tabela ex: 1 - José/ 2- João/etc)

5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato 
O total de votos nulos
O total de votos em branco 
A porcentagem de votos nulos sobre o total de votos
A porcentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero. 

'''

candidato1 = candidato2 = candidato3 = candidato4 = nulo = branco = 0

while True:
    voto = input("Digite o código do candidato ou 0 para sair: ")
    if voto.isnumeric():
        voto = int(voto)

        if voto == 0:
            break
        elif voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        elif voto == 4:
            candidato4+= 1
        elif voto == 5:
            nulo += 1
        elif voto == 6:
            branco += 1
    else:
        print("Digite apenas números!")

total_votos = candidato1 + candidato2 + candidato3 + candidato4 + nulo + branco

percentual_nulos = (nulo / total_votos) * 100
percentual_brancos = (branco / total_votos) * 100

print(f"Total de votos para o Bononaro: {candidato1}")
print(f"Total de votos para o Lulinha: {candidato2}")
print(f"Total de votos para o Padre de Festa Junina: {candidato3}")
print(f"Total de votos para o Trump: {candidato4}")
print(f"Total de votos nulos: {nulo}")
print(f"Total de votos em branco: {branco}")
print(f"Percentual de votos nulos sobre o total de votos: {percentual_nulos:.2f}%")
print(f"Percentual de votos em branco sobre o total de votos: {percentual_brancos:.2f}%")
