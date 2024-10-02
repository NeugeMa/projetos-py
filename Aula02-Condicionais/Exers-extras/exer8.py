'''Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na tela dizendo se está “quente”, 
“frio” ou “agradável”.'''

temperatura = float(input("Qual é a temperatura atual? "))

# Definindo valores
limite_quente = 25
limite_frio = 15

if temperatura > limite_quente:
    print("Está quente!")
elif temperatura < limite_frio:
    print("Está frio!")
else:
    print("Está agradável!")
