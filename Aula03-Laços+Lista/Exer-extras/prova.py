'''
Exercício: Calculadora de Média

Escreva um programa que pede ao usuário para inserir as notas de um aluno e calcula a média delas. O programa deve continuar pedindo notas 
até que o usuário digite um valor especial para indicar que terminou de inserir as notas. 
Por exemplo, você pode usar o valor -1 para indicar o fim da entrada das notas. O programa deve então exibir a média das notas inseridas.

Regras:

1. O programa deve solicitar as notas ao usuário repetidamente até que ele insira o valor especial indicando o fim das entradas.
2. O valor especial para indicar o fim das entradas não deve ser incluído no cálculo da média.

Se o usuário inserir um valor inválido (por exemplo, uma nota menor que 0 ou maior que 10), o programa deve exibir uma mensagem de erro e 
pedir ao usuário para inserir a nota novamente.
Isso exigirá o uso de um loop while para continuar solicitando as notas até que o usuário decida parar, bem como condicionais para verificar 
se as notas são válidas e calcular a média.
'''
qtd = 1
notas = []
especial = 'sair'

print("Olá, seja bem-vindo! Vamos calcular suas médias?")
print("Opções, para sair do loop digite 'sair' ")
while True:
    nota = input(f"Digite sua {qtd} nota (ou '{especial}' para sair): ")
    if nota == especial:
        break
    nota = float(nota)
    if nota < 0 or nota > 10:
        print("Valor inválido! Insira uma nota entre 0 e 10.")
        continue
    notas.append(nota)
    qtd += 1

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"A média das notas inseridas é: {media}")
else:
    print("Nenhuma nota foi inserida.")
