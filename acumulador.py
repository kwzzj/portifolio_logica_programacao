import os
os.system("cls || clear")

acumulador=0
for contador in range(1,4):
    valor = float(input(f"Digite o valor do item {contador}: "))
    acumulador += valor
print(acumulador)
