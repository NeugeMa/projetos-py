#Contar a quantidade de caracteres:
vogais = 0
nome = 'mari'

for char in nome:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u': 
        vogais += 1
print(f"Há vogais {vogais} e {len(nome) - vogais }"
      f" consoantes em {nome}")
     