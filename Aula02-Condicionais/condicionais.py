#Condicionais
idade = int(input("Para entrar no site, digite sua idade: "))
if idade < 18:
    print("Você é menor de idade e não pode acessar o site.")
else: 
    print("Bem vindo a Zé Delivery")

#Condição utilizando - OR 
idoso = input("Você é idoso? ")
gestante = input("Você está grávida?")
if idoso == 'sim' or gestante == 'sim': 
    print("Pode estacionar!!")

#Condição utilizando - AND | só irá ser terminada quando ambas condições sejam verdadeiras 
idoso = input("Você é idoso? ")
cartao = input("Você tem o cartão? ")
if idoso == 'sim': 
    if cartao == 'sim':
        print("Estacionar")

#Exercício: Faça um código que mostre as vogais utilizando tudo que aprendemos 
vogal = input("Digite uma letra: ")
if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u": #utilizando o or 
    print("Isso aí, você acertou a letra 😎")
else: 
    print("Seu burro!! Você errou")

#Outra opção de resolução:
vogal = input("Digite uma letra: ")
if vogal == "a": 
    print("Isso é uma vogal")
elif vogal == "e":  
    print("Isso é uma vogal")
elif vogal == "i":  
    print("Isso é uma vogal")
elif vogal == "o":  
    print("Isso é uma vogal")
elif vogal == "u":  
    print("Isso é uma vogal")
else: 
    print("Isso é uma consoante")

#Declarando se um aluno está reprovado/aprovado/exame
nota = int(input("Digite sua nota: "))
if nota >= 6:
    print(f"Parabéns você está aprovado, atingindo a média final {nota}")
elif nota >=4:
    print ("Exame")
else:
    print("Reprovado!")

#Declarando o imposto de renda 
salario = float(input("Digite seu sálario atual: "))
if salario<1903.98: 
    agiota = 0 #Porcentagem agiota 
elif salario <= 2826.65: 
    agiota = 0.075 #Porcentagem agiota
elif salario <= 3751.05:
    agiota = 0.15 #Porcentagem agiota
elif salario <= 4664.68:
    agiota = 0.225 #Porcentagem agiota
  
else: 
    agiota = 0.275 #Porcentagem agiota
    desconto = salario*agiota
    salario = salario - desconto
    print(f" O seu salário com desconto é de {desconto} será {salario}!!")

'''____'''

#Exercício Multa - 20/03
''' 
Até 100km por hora -> você está isento 
Até 120km por hora -> você paga 20% de velocidade | 0.2  
Até 150km por hora -> você paga 20% de 120 + 30% de velocidade | 0.3 
Se for mais que 150 -> 20%120+30% 150+40% velocidade 
'''

velocidade = int(input("Diga o valor da velocidade: ")) 
if velocidade <= 100: #Até 100km km/h -> você está isento 
    multa = 0 
    print ("Você esta isento") 

else: 
    if velocidade <= 120:  #Até 120 km/h  -> Você paga 20%
        multa = 0.2*velocidade 
        print (f"Sua multa é de {multa}")

    elif velocidade <= 150: #Até 150 km/h -> Você paga 20% de 120 + 30% 
        multa = 0.2*120 + 0.3*velocidade
        print (f"Sua multa é de {multa}") 

    elif velocidade > 150: 
        multa = 0.2*120 + 0.3*150 + 0.4*velocidade
        print (f"Sua multa é de {multa}") 

#Resolução Professor: 
v = int(input("Diga o valor da velocidade: ")) 
if v <= 100: 
    multa = 0 

elif  v <= 120: 
    multa = 0.2*v 
elif v <= 150: 
    multa = 0.2*120 + 0.3*v 

else: 
    multa = 0.2*120 + 0.3*150 + 0.4*v 
    print(f"A multa será de {multa}")


#Exercício Par & ímpar 
num = 2 
if num%2 == 0: #Usamos % por que ele irá dividir o número até achar 0 ou 1 
    print(f"{num} é par pois {num}%{2} = {num%2}")
else: 
    print(f"{num} é impar pois {num}%{2} = {num%2}")

#Minha Resolução:  
#Pedir 5 números e conferir se são pares ou ímpares
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

par = 0 #Vai ser nosso contador 
impar = 5-par

if  num1%2 == 0: 
    par += 1
if num2%2 == 0: 
    par += 1
if num3%2 == 0: 
    par += 1
if num4%2 == 0: 
    par += 1
if num5%2 == 0: 
    par += 1
print(f"A quantidades de pares é de {par} | e de ímpares é de {impar}")

    