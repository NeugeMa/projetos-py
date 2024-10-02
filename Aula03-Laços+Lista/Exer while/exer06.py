'''
Faça um programa que leia o nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    user = input("Digite seu nome de usuário: ")
    senha = input("Digite agora sua senha: ")
    
    if user != senha:
        print("Usuário e senha foram definidos com sucesso.")
        break
    else:
        print("Erro: A senha não pode ser igual ao nome do usuário. Por favor, tente novamente.")