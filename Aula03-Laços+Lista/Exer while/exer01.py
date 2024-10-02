''' Faça um programa que peça a nota, entre 0 à 10. Mostre a mensagem caso o valor seja inválido 
e continue pedindo até que o usuário informe um valor válido.'''

while True: 
    nota = input("Digite sua nota: ")
    if nota.isnumeric():
        if int(nota) >= 0 and int(nota) <= 10: 
            nota = int(nota)
            print(f"Essa é sua nota {nota}")
            break 
    print("Resposta inválida")
