'''
Supondo que a população de um país. A seja da ordem de 80000 habitantes com uma taxa anual de crescimento 
de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 

Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população
do país B, mantidas as taxas de crescimento. 
'''

a = 80000
b = 200000
ano = 0

while a < b: 
    a += a*1.03
    b += b*1.015
    ano += 1 
    print(f"O número de anos foi {ano}") 

#Resolução Professor:
'''
ano:80
ano 1: 80 + 80.3/100 -> 80(1+0,03) | 80.1,03
ano 2: 80.1,03 + 80.1,03.0,03      M:A=80.103m
       80.1,03(1+0,03)             B=200.1,015m
       80(1+0,03)                  A=B
                                   80/80.1,03m/1,05m = 200/80
'''

a = 80
b = 200
ano = 0

while a < b: 
    a*=1.03     #Vezes igual
    b*=1.015
    ano += 1 
    print(f"Seu resultado foi de {ano}")