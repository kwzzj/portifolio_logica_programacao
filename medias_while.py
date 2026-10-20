import os
os.system("cls || clear")

contador=0
nota=0
while (nota!=-1):
    nota= float(input("Digite um número: "))
    contador += 1
print(f"Você digitou {contador -1} vezes")    
print(f"A média é {(contador+contador)/contador: .0f}")


