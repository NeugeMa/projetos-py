''' 

'''

num1 =  int(input("Digite o seu primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while num2 > num1: 
    print("Escreva número, por favor!")
    num1 =  int(input("Digite o seu primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

else: 
    for i in range(num1, num2, 1):
        print(i)

#Resolução Professor:
num1 =  int(input("Digite o seu primeiro número: "))
num2 = int(input("Digite o segundo número: "))   

while num2 < num1:
    print(num1)
    num2+=1