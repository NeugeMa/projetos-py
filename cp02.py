#Resolução Professor:

vinho01 = 'Chapinha'
preco1 = 10
qtd01 = 0

vinho02 = 'Sangue de Boi'
preco2 = 20
qtd02 = 0

vinho03 = 'Catuaba'
preco3 = 30
qtd03 = 0

valor = 0
frete = 10

print("Seja bem-vindo à Vinharia Agnello")
ano = input("Diga o seu ano de nascimento: ")

while not ano.isnumeric():
    ano = input("Diga o seu ano de nascimento: ")
ano = int(ano)

idade = 2024 -18
if idade >= 18: 
    end = input("Digite seu endereço: ")
    opcao = input(f"Qual vinho você quer? \n {vinho01} : {preco1}\n "
                  f"{vinho02} : {preco2} \n {vinho03} : {preco3}")

    while opcao != vinho01 and opcao != vinho02 and opcao != vinho03: 
        print("Opção Inválida")
        opcao = input(f"Qual vinho você quer? \n {vinho01} : {preco1}\n "
                  f"{vinho02} : {preco2} \n {vinho03} : {preco3}")

    qtd = input(f"Quantos vinhos {opcao}? ")
    while not qtd.isnumeric(): 
        print("Deve ser número!")
    qtd = int(qtd)

        if opcao == vinho01: 
            preco1 == qtd * preco1
            qtd01 += qtd 
        elif opcao == vinho02: 
            preco2 == qtd * preco2
            qtd02 += qtd 

        else: 
            preco = qtd*preco3
            qtd03 += qtd 

        valor += preco 
        resposta = input("Você quer comprar mais vinhos? s/n -> ")
        while not (resposta == 's' or resposta == 'n'):
            print("Opção Inválida")
            resposta = input("Você quer comprar mais vinhos? s/n -> ")
        if resposta == 'n': 
                break 
    if valor >= 500:
        print("Frete grátis!")
    else: 
        valor += frete
    print("Obrigada por comprar na Agnelo!"\n 
            f"Você comprou {qtd1} de {vinho01}, {qtd02} de {vinho02} e {qtd03} de {vinho03} pelo R${valor:.2f}\n"
            f"e será entregue em {end}")
else:
    print("Tchau criança") 