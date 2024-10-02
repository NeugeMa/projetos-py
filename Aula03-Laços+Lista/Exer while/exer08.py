'''
A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n-ésimo termo.
'''
numero = int(input("Digite um número: "))
a = 1
b = 1 
i = 2 
n = 17
print(a)
print(b)
while i < numero: 
    c = a + b
    a = b
    b = c
    print(c)

