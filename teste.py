import os
os.system('cls || clear')

print("Digite a sua idade: ")
idade= input()
if idade <16:
    print("Não pode entrar")
elif idade == 16 or 17:
    print("Pode entrar com os pais") 
else:
    print("Pode entrar")       