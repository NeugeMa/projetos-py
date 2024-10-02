'''
4. Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.
'''

continuar = "sim"
while continuar == "sim":
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    print(f"A soma dos números é {num1 + num2}")
    continuar = input("Deseja continuar? (sim/não): ")