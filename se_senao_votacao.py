import os
os.system('cls || clear')

print("Escreva a sua idade.")
idade = int(input())
if (idade >= 16):
    print("Você pode votar.")
    if (idade >= 18):
        print("Voto obrigatório")
    if (idade >= 16) and (idade < 18):
        print("Voto facultativo")    